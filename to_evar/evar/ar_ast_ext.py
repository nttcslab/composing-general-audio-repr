"""
"""

import logging
try:
    from evar.ar_ast import torch, AR_AST
except Exception as e:
    logging.error(f'Make your copy of AST under external folder. Check ar_ast.py for the details.')
    class AR_AST:
        pass


class AR_AST_Fusion(AR_AST):
    def forward(self, batch_audio):
        layers = self.cfg['ast_layers']
        layers = [layers] if isinstance(layers, (int)) else layers

        x = self.to_feature(batch_audio)
        x = self.normalize_spectrogram(x)

        embeds = []

        # from the original forward()
        x = x.unsqueeze(1)
        x = x.transpose(2, 3)

        B = x.shape[0]
        x = self.backbone.v.patch_embed(x)
        cls_tokens = self.backbone.v.cls_token.expand(B, -1, -1)
        dist_token = self.backbone.v.dist_token.expand(B, -1, -1)
        x = torch.cat((cls_tokens, dist_token, x), dim=1)
        x = x + self.backbone.v.pos_embed
        x = self.backbone.v.pos_drop(x)
        for l, blk in enumerate(self.backbone.v.blocks):
            x = blk(x)
            if l in layers:
                xdash = self.backbone.v.norm(x)
                xdash = (xdash[:, 0] + xdash[:, 1]) / 2
                embeds.append(xdash)
        return torch.hstack(embeds)
