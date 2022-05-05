"""
"""

from evar.ar_vggish import torch, AR_VGGish
from evar.gp_vggish import GeneralPurposeVGGish


class AR_VGGish_Fusion(AR_VGGish):
    def __init__(self, cfg):
        super().__init__(cfg=cfg, vggish_class=GeneralPurposeVGGish)

    def encode_frames(self, batch_audio):
        layers = self.cfg['vggish_layers'] # [1, 4, 7, 9, 12, 14, 17, 19, 21]
        layers = [layers] if isinstance(layers, (int)) else layers
    
        X = self.to_audio_features(batch_audio)
        Xs = [self.vggish.encode_frames(X[:, i:i+1], layers=layers) for i in range(X.shape[1])]
        X = torch.stack(Xs, dim=-1) # [B, D, T] x Sec_frame -> [B, D, T, Sec_frame]
        B, D, T, Frame = X.shape
        X = X.reshape(B, D, T*Frame) # [B, D, T, Sec_frame] -> [B, D, T*Sec_frame]
        return X

