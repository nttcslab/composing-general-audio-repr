"""PANNs' CNN14 extensions.
"""

from evar.ar_cnn14 import AR_Cnn14
from evar.ar_base import temporal_pooling
from evar.gp_cnn14 import GeneralPurposeCnn14


class AR_Cnn14_Fusion(AR_Cnn14):

    def __init__(self, cfg):
        super().__init__(cfg=cfg)
        # Create a GeneralPurposeCnn14 instance with Cnn14 weights
        weights = self.body.state_dict()
        self.body = GeneralPurposeCnn14()
        self.body.load_state_dict(weights)

    def encode_frames(self, batch_audio):
        layers = self.cfg['cnn14_layers']
        layers = [layers] if isinstance(layers, (int)) else layers

        x = self.feature_extractor(batch_audio)            # (B, 1, T, F(mel_bins))
        x = self.body.encode_frame(x, layers=layers)       # (B, D, T)
        return x

    def forward(self, batch_audio):
        frame_embeddings = self.encode_frames(batch_audio) # (B, D, T)
        return temporal_pooling(self, frame_embeddings)    # (B, D)
