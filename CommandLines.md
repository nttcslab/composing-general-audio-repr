# Command lines for reproducing our paper

We used the following command lines to get results on the paper.

## PANNs' CNN14

```sh
(Original CNN14)
python 2pass_lineareval.py config/cnn14.yaml cremad
python 2pass_lineareval.py config/cnn14.yaml voxforge
python 2pass_lineareval.py config/cnn14.yaml esc50
python 2pass_lineareval.py config/cnn14.yaml gtzan
python 2pass_lineareval.py config/cnn14.yaml fsd50k
python 2pass_lineareval.py config/cnn14.yaml nsynth --lr=0.00001
python 2pass_lineareval.py config/cnn14.yaml nspitch
python 2pass_lineareval.py config/cnn14.yaml surge
python 2pass_lineareval.py config/cnn14.yaml vc1
python 2pass_lineareval.py config/cnn14.yaml spcv2
python 2pass_lineareval.py config/cnn14.yaml us8k

(CNN14-Fusion#3#6)
python 2pass_lineareval.py config/cnn14_fusion.yaml cremad +name=AR_Cnn14_Fusion36
python 2pass_lineareval.py config/cnn14_fusion.yaml voxforge +name=AR_Cnn14_Fusion36
python 2pass_lineareval.py config/cnn14_fusion.yaml esc50 +name=AR_Cnn14_Fusion36
python 2pass_lineareval.py config/cnn14_fusion.yaml gtzan batch_size=16,+name=AR_Cnn14_Fusion36
python 2pass_lineareval.py config/cnn14_fusion.yaml spcv2 +name=AR_Cnn14_Fusion36
python 2pass_lineareval.py config/cnn14_fusion.yaml us8k +name=AR_Cnn14_Fusion36
python 2pass_lineareval.py config/cnn14_fusion.yaml nsynth --lr=0.00001 +name=AR_Cnn14_Fusion36
python 2pass_lineareval.py config/cnn14_fusion.yaml surge --lr=0.00003 +name=AR_Cnn14_Fusion36
python 2pass_lineareval.py config/cnn14_fusion.yaml vc1 batch_size=96,+name=AR_Cnn14_Fusion36

(For probing layer performances)
python 2pass_lineareval.py config/cnn14_fusion.yaml cremad +name=AR_Cnn14_L1,cnn14_layers=1
python 2pass_lineareval.py config/cnn14_fusion.yaml cremad +name=AR_Cnn14_L2,cnn14_layers=2
python 2pass_lineareval.py config/cnn14_fusion.yaml cremad +name=AR_Cnn14_L3,cnn14_layers=3
python 2pass_lineareval.py config/cnn14_fusion.yaml cremad +name=AR_Cnn14_L4,cnn14_layers=4
python 2pass_lineareval.py config/cnn14_fusion.yaml cremad +name=AR_Cnn14_L5,cnn14_layers=5
python 2pass_lineareval.py config/cnn14_fusion.yaml cremad +name=AR_Cnn14_L6,cnn14_layers=6
python 2pass_lineareval.py config/cnn14_fusion.yaml voxforge +name=AR_Cnn14_L1,cnn14_layers=1
python 2pass_lineareval.py config/cnn14_fusion.yaml voxforge +name=AR_Cnn14_L2,cnn14_layers=2
python 2pass_lineareval.py config/cnn14_fusion.yaml voxforge +name=AR_Cnn14_L3,cnn14_layers=3
python 2pass_lineareval.py config/cnn14_fusion.yaml voxforge +name=AR_Cnn14_L4,cnn14_layers=4
python 2pass_lineareval.py config/cnn14_fusion.yaml voxforge +name=AR_Cnn14_L5,cnn14_layers=5
python 2pass_lineareval.py config/cnn14_fusion.yaml voxforge +name=AR_Cnn14_L6,cnn14_layers=6
python 2pass_lineareval.py config/cnn14_fusion.yaml esc50 +name=AR_Cnn14_L1,cnn14_layers=1
python 2pass_lineareval.py config/cnn14_fusion.yaml esc50 +name=AR_Cnn14_L2,cnn14_layers=2
python 2pass_lineareval.py config/cnn14_fusion.yaml esc50 +name=AR_Cnn14_L3,cnn14_layers=3
python 2pass_lineareval.py config/cnn14_fusion.yaml esc50 +name=AR_Cnn14_L4,cnn14_layers=4
python 2pass_lineareval.py config/cnn14_fusion.yaml esc50 +name=AR_Cnn14_L5,cnn14_layers=5
python 2pass_lineareval.py config/cnn14_fusion.yaml esc50 +name=AR_Cnn14_L6,cnn14_layers=6
python 2pass_lineareval.py config/cnn14_fusion.yaml gtzan batch_size=16,+name=AR_Cnn14_L1,cnn14_layers=1
python 2pass_lineareval.py config/cnn14_fusion.yaml gtzan batch_size=16,+name=AR_Cnn14_L2,cnn14_layers=2
python 2pass_lineareval.py config/cnn14_fusion.yaml gtzan batch_size=16,+name=AR_Cnn14_L3,cnn14_layers=3
python 2pass_lineareval.py config/cnn14_fusion.yaml gtzan batch_size=16,+name=AR_Cnn14_L4,cnn14_layers=4
python 2pass_lineareval.py config/cnn14_fusion.yaml gtzan batch_size=16,+name=AR_Cnn14_L5,cnn14_layers=5
python 2pass_lineareval.py config/cnn14_fusion.yaml gtzan batch_size=16,+name=AR_Cnn14_L6,cnn14_layers=6
python 2pass_lineareval.py config/cnn14_fusion.yaml spcv2 +name=AR_Cnn14_L1,cnn14_layers=1
python 2pass_lineareval.py config/cnn14_fusion.yaml spcv2 +name=AR_Cnn14_L2,cnn14_layers=2
python 2pass_lineareval.py config/cnn14_fusion.yaml spcv2 +name=AR_Cnn14_L3,cnn14_layers=3
python 2pass_lineareval.py config/cnn14_fusion.yaml spcv2 +name=AR_Cnn14_L4,cnn14_layers=4
python 2pass_lineareval.py config/cnn14_fusion.yaml spcv2 +name=AR_Cnn14_L5,cnn14_layers=5
python 2pass_lineareval.py config/cnn14_fusion.yaml spcv2 +name=AR_Cnn14_L6,cnn14_layers=6
python 2pass_lineareval.py config/cnn14_fusion.yaml us8k +name=AR_Cnn14_L1,cnn14_layers=1
python 2pass_lineareval.py config/cnn14_fusion.yaml us8k +name=AR_Cnn14_L2,cnn14_layers=2
python 2pass_lineareval.py config/cnn14_fusion.yaml us8k +name=AR_Cnn14_L3,cnn14_layers=3
python 2pass_lineareval.py config/cnn14_fusion.yaml us8k +name=AR_Cnn14_L4,cnn14_layers=4
python 2pass_lineareval.py config/cnn14_fusion.yaml us8k +name=AR_Cnn14_L5,cnn14_layers=5
python 2pass_lineareval.py config/cnn14_fusion.yaml us8k +name=AR_Cnn14_L6,cnn14_layers=6
python 2pass_lineareval.py config/cnn14_fusion.yaml nsynth --lr=0.00001 +name=AR_Cnn14_L1,cnn14_layers=1
python 2pass_lineareval.py config/cnn14_fusion.yaml nsynth --lr=0.00001 +name=AR_Cnn14_L2,cnn14_layers=2
python 2pass_lineareval.py config/cnn14_fusion.yaml nsynth --lr=0.00001 +name=AR_Cnn14_L3,cnn14_layers=3
python 2pass_lineareval.py config/cnn14_fusion.yaml nsynth --lr=0.00001 +name=AR_Cnn14_L4,cnn14_layers=4
python 2pass_lineareval.py config/cnn14_fusion.yaml nsynth --lr=0.00001 +name=AR_Cnn14_L5,cnn14_layers=5
python 2pass_lineareval.py config/cnn14_fusion.yaml nsynth --lr=0.00001 +name=AR_Cnn14_L6,cnn14_layers=6
python 2pass_lineareval.py config/cnn14_fusion.yaml surge --lr=0.00003 +name=AR_Cnn14_L1,cnn14_layers=1
python 2pass_lineareval.py config/cnn14_fusion.yaml surge --lr=0.00003 +name=AR_Cnn14_L2,cnn14_layers=2
python 2pass_lineareval.py config/cnn14_fusion.yaml surge --lr=0.00003 +name=AR_Cnn14_L3,cnn14_layers=3
python 2pass_lineareval.py config/cnn14_fusion.yaml surge --lr=0.00003 +name=AR_Cnn14_L4,cnn14_layers=4
python 2pass_lineareval.py config/cnn14_fusion.yaml surge --lr=0.00003 +name=AR_Cnn14_L5,cnn14_layers=5
python 2pass_lineareval.py config/cnn14_fusion.yaml surge --lr=0.00003 +name=AR_Cnn14_L6,cnn14_layers=6
python 2pass_lineareval.py config/cnn14_fusion.yaml vc1 batch_size=96,+name=AR_Cnn14_L1,cnn14_layers=1
python 2pass_lineareval.py config/cnn14_fusion.yaml vc1 batch_size=96,+name=AR_Cnn14_L2,cnn14_layers=2
python 2pass_lineareval.py config/cnn14_fusion.yaml vc1 batch_size=96,+name=AR_Cnn14_L3,cnn14_layers=3
python 2pass_lineareval.py config/cnn14_fusion.yaml vc1 batch_size=96,+name=AR_Cnn14_L4,cnn14_layers=4
python 2pass_lineareval.py config/cnn14_fusion.yaml vc1 batch_size=96,+name=AR_Cnn14_L5,cnn14_layers=5
python 2pass_lineareval.py config/cnn14_fusion.yaml vc1 batch_size=96,+name=AR_Cnn14_L6,cnn14_layers=6
```

# VGGish

```sh
(Original VGGish)
python 2pass_lineareval.py config/vggish.yaml cremad
python 2pass_lineareval.py config/vggish.yaml voxforge
python 2pass_lineareval.py config/vggish.yaml esc50 --lr=0.003
python 2pass_lineareval.py config/vggish.yaml spcv2
python 2pass_lineareval.py config/vggish.yaml us8k
python 2pass_lineareval.py config/vggish.yaml nsynth
python 2pass_lineareval.py config/vggish.yaml surge
python 2pass_lineareval.py config/vggish.yaml vc1 --lr=0.0005
python 2pass_lineareval.py config/vggish.yaml gtzan batch_size=128

(VGGish-Fusion#10#15)
python 2pass_lineareval.py config/vggish_fusion.yaml cremad +name=AR_VGGish_Fusion1015
python 2pass_lineareval.py config/vggish_fusion.yaml voxforge +name=AR_VGGish_Fusion1015
python 2pass_lineareval.py config/vggish_fusion.yaml esc50 +name=AR_VGGish_Fusion1015
python 2pass_lineareval.py config/vggish_fusion.yaml spcv2 +name=AR_VGGish_Fusion1015
python 2pass_lineareval.py config/vggish_fusion.yaml us8k +name=AR_VGGish_Fusion1015
python 2pass_lineareval.py config/vggish_fusion.yaml nsynth +name=AR_VGGish_Fusion1015
python 2pass_lineareval.py config/vggish_fusion.yaml surge --lr=0.0001 +name=AR_VGGish_Fusion1015
python 2pass_lineareval.py config/vggish_fusion.yaml vc1 --lr=0.0005 +name=AR_VGGish_Fusion1015
python 2pass_lineareval.py config/vggish_fusion.yaml gtzan batch_size=128,+name=AR_VGGish_Fusion1015

(For probing layer performances)
python 2pass_lineareval.py config/vggish_fusion.yaml cremad +name=AR_VGGish_L1,vggish_layers=1
python 2pass_lineareval.py config/vggish_fusion.yaml cremad +name=AR_VGGish_L4,vggish_layers=4
python 2pass_lineareval.py config/vggish_fusion.yaml cremad +name=AR_VGGish_L7,vggish_layers=7
python 2pass_lineareval.py config/vggish_fusion.yaml cremad +name=AR_VGGish_L9,vggish_layers=9
python 2pass_lineareval.py config/vggish_fusion.yaml cremad +name=AR_VGGish_L12,vggish_layers=12
python 2pass_lineareval.py config/vggish_fusion.yaml cremad +name=AR_VGGish_L14,vggish_layers=14
python 2pass_lineareval.py config/vggish_fusion.yaml cremad +name=AR_VGGish_L17,vggish_layers=17
python 2pass_lineareval.py config/vggish_fusion.yaml cremad +name=AR_VGGish_L19,vggish_layers=19
python 2pass_lineareval.py config/vggish_fusion.yaml cremad +name=AR_VGGish_L21,vggish_layers=21
python 2pass_lineareval.py config/vggish_fusion.yaml voxforge +name=AR_VGGish_L1,vggish_layers=1
python 2pass_lineareval.py config/vggish_fusion.yaml voxforge +name=AR_VGGish_L4,vggish_layers=4
python 2pass_lineareval.py config/vggish_fusion.yaml voxforge +name=AR_VGGish_L7,vggish_layers=7
python 2pass_lineareval.py config/vggish_fusion.yaml voxforge +name=AR_VGGish_L9,vggish_layers=9
python 2pass_lineareval.py config/vggish_fusion.yaml voxforge +name=AR_VGGish_L12,vggish_layers=12
python 2pass_lineareval.py config/vggish_fusion.yaml voxforge +name=AR_VGGish_L14,vggish_layers=14
python 2pass_lineareval.py config/vggish_fusion.yaml voxforge +name=AR_VGGish_L17,vggish_layers=17
python 2pass_lineareval.py config/vggish_fusion.yaml voxforge +name=AR_VGGish_L19,vggish_layers=19
python 2pass_lineareval.py config/vggish_fusion.yaml voxforge +name=AR_VGGish_L21,vggish_layers=21
python 2pass_lineareval.py config/vggish_fusion.yaml esc50 +name=AR_VGGish_L1,vggish_layers=1
python 2pass_lineareval.py config/vggish_fusion.yaml esc50 +name=AR_VGGish_L4,vggish_layers=4
python 2pass_lineareval.py config/vggish_fusion.yaml esc50 +name=AR_VGGish_L7,vggish_layers=7
python 2pass_lineareval.py config/vggish_fusion.yaml esc50 +name=AR_VGGish_L9,vggish_layers=9
python 2pass_lineareval.py config/vggish_fusion.yaml esc50 +name=AR_VGGish_L12,vggish_layers=12
python 2pass_lineareval.py config/vggish_fusion.yaml esc50 +name=AR_VGGish_L14,vggish_layers=14
python 2pass_lineareval.py config/vggish_fusion.yaml esc50 +name=AR_VGGish_L17,vggish_layers=17
python 2pass_lineareval.py config/vggish_fusion.yaml esc50 +name=AR_VGGish_L19,vggish_layers=19
python 2pass_lineareval.py config/vggish_fusion.yaml esc50 +name=AR_VGGish_L21,vggish_layers=21
python 2pass_lineareval.py config/vggish_fusion.yaml spcv2 +name=AR_VGGish_L1,vggish_layers=1
python 2pass_lineareval.py config/vggish_fusion.yaml spcv2 +name=AR_VGGish_L4,vggish_layers=4
python 2pass_lineareval.py config/vggish_fusion.yaml spcv2 +name=AR_VGGish_L7,vggish_layers=7
python 2pass_lineareval.py config/vggish_fusion.yaml spcv2 +name=AR_VGGish_L9,vggish_layers=9
python 2pass_lineareval.py config/vggish_fusion.yaml spcv2 +name=AR_VGGish_L12,vggish_layers=12
python 2pass_lineareval.py config/vggish_fusion.yaml spcv2 +name=AR_VGGish_L14,vggish_layers=14
python 2pass_lineareval.py config/vggish_fusion.yaml spcv2 +name=AR_VGGish_L17,vggish_layers=17
python 2pass_lineareval.py config/vggish_fusion.yaml spcv2 +name=AR_VGGish_L19,vggish_layers=19
python 2pass_lineareval.py config/vggish_fusion.yaml spcv2 +name=AR_VGGish_L21,vggish_layers=21
python 2pass_lineareval.py config/vggish_fusion.yaml us8k +name=AR_VGGish_L1,vggish_layers=1
python 2pass_lineareval.py config/vggish_fusion.yaml us8k +name=AR_VGGish_L4,vggish_layers=4
python 2pass_lineareval.py config/vggish_fusion.yaml us8k +name=AR_VGGish_L7,vggish_layers=7
python 2pass_lineareval.py config/vggish_fusion.yaml us8k +name=AR_VGGish_L9,vggish_layers=9
python 2pass_lineareval.py config/vggish_fusion.yaml us8k +name=AR_VGGish_L12,vggish_layers=12
python 2pass_lineareval.py config/vggish_fusion.yaml us8k +name=AR_VGGish_L14,vggish_layers=14
python 2pass_lineareval.py config/vggish_fusion.yaml us8k +name=AR_VGGish_L17,vggish_layers=17
python 2pass_lineareval.py config/vggish_fusion.yaml us8k +name=AR_VGGish_L19,vggish_layers=19
python 2pass_lineareval.py config/vggish_fusion.yaml us8k +name=AR_VGGish_L21,vggish_layers=21
python 2pass_lineareval.py config/vggish_fusion.yaml nsynth +name=AR_VGGish_L1,vggish_layers=1
python 2pass_lineareval.py config/vggish_fusion.yaml nsynth +name=AR_VGGish_L4,vggish_layers=4
python 2pass_lineareval.py config/vggish_fusion.yaml nsynth +name=AR_VGGish_L7,vggish_layers=7
python 2pass_lineareval.py config/vggish_fusion.yaml nsynth +name=AR_VGGish_L9,vggish_layers=9
python 2pass_lineareval.py config/vggish_fusion.yaml nsynth +name=AR_VGGish_L12,vggish_layers=12
python 2pass_lineareval.py config/vggish_fusion.yaml nsynth +name=AR_VGGish_L14,vggish_layers=14
python 2pass_lineareval.py config/vggish_fusion.yaml nsynth +name=AR_VGGish_L17,vggish_layers=17
python 2pass_lineareval.py config/vggish_fusion.yaml nsynth +name=AR_VGGish_L19,vggish_layers=19
python 2pass_lineareval.py config/vggish_fusion.yaml nsynth +name=AR_VGGish_L21,vggish_layers=21
python 2pass_lineareval.py config/vggish_fusion.yaml surge +name=AR_VGGish_L1,vggish_layers=1
python 2pass_lineareval.py config/vggish_fusion.yaml surge +name=AR_VGGish_L4,vggish_layers=4
python 2pass_lineareval.py config/vggish_fusion.yaml surge +name=AR_VGGish_L7,vggish_layers=7
python 2pass_lineareval.py config/vggish_fusion.yaml surge +name=AR_VGGish_L9,vggish_layers=9
python 2pass_lineareval.py config/vggish_fusion.yaml surge +name=AR_VGGish_L12,vggish_layers=12
python 2pass_lineareval.py config/vggish_fusion.yaml surge +name=AR_VGGish_L14,vggish_layers=14
python 2pass_lineareval.py config/vggish_fusion.yaml surge +name=AR_VGGish_L17,vggish_layers=17
python 2pass_lineareval.py config/vggish_fusion.yaml surge +name=AR_VGGish_L19,vggish_layers=19
python 2pass_lineareval.py config/vggish_fusion.yaml surge +name=AR_VGGish_L21,vggish_layers=21
python 2pass_lineareval.py config/vggish_fusion.yaml vc1 --lr=0.0005 +name=AR_VGGish_L1,vggish_layers=1
python 2pass_lineareval.py config/vggish_fusion.yaml vc1 --lr=0.0005 +name=AR_VGGish_L4,vggish_layers=4
python 2pass_lineareval.py config/vggish_fusion.yaml vc1 --lr=0.0005 +name=AR_VGGish_L7,vggish_layers=7
python 2pass_lineareval.py config/vggish_fusion.yaml vc1 --lr=0.0005 +name=AR_VGGish_L9,vggish_layers=9
python 2pass_lineareval.py config/vggish_fusion.yaml vc1 --lr=0.0005 +name=AR_VGGish_L12,vggish_layers=12
python 2pass_lineareval.py config/vggish_fusion.yaml vc1 --lr=0.0005 +name=AR_VGGish_L14,vggish_layers=14
python 2pass_lineareval.py config/vggish_fusion.yaml vc1 --lr=0.0005 +name=AR_VGGish_L17,vggish_layers=17
python 2pass_lineareval.py config/vggish_fusion.yaml vc1 --lr=0.0005 +name=AR_VGGish_L19,vggish_layers=19
python 2pass_lineareval.py config/vggish_fusion.yaml vc1 --lr=0.0005 +name=AR_VGGish_L21,vggish_layers=21
python 2pass_lineareval.py config/vggish_fusion.yaml gtzan batch_size=128,+name=AR_VGGish_L1,vggish_layers=1
python 2pass_lineareval.py config/vggish_fusion.yaml gtzan batch_size=128,+name=AR_VGGish_L4,vggish_layers=4
python 2pass_lineareval.py config/vggish_fusion.yaml gtzan batch_size=128,+name=AR_VGGish_L7,vggish_layers=7
python 2pass_lineareval.py config/vggish_fusion.yaml gtzan batch_size=128,+name=AR_VGGish_L9,vggish_layers=9
python 2pass_lineareval.py config/vggish_fusion.yaml gtzan batch_size=128,+name=AR_VGGish_L12,vggish_layers=12
python 2pass_lineareval.py config/vggish_fusion.yaml gtzan batch_size=128,+name=AR_VGGish_L14,vggish_layers=14
python 2pass_lineareval.py config/vggish_fusion.yaml gtzan batch_size=128,+name=AR_VGGish_L17,vggish_layers=17
python 2pass_lineareval.py config/vggish_fusion.yaml gtzan batch_size=128,+name=AR_VGGish_L19,vggish_layers=19
python 2pass_lineareval.py config/vggish_fusion.yaml gtzan batch_size=128,+name=AR_VGGish_L21,vggish_layers=21
```

# AST

```sh
(Original AST)
python 2pass_lineareval.py config/ast.yaml cremad
python 2pass_lineareval.py config/ast.yaml voxforge
python 2pass_lineareval.py config/ast.yaml esc50
python 2pass_lineareval.py config/ast.yaml gtzan batch_size=12
python 2pass_lineareval.py config/ast.yaml spcv2
python 2pass_lineareval.py config/ast.yaml us8k
python 2pass_lineareval.py config/ast.yaml surge --lr=0.0001
python 2pass_lineareval.py config/ast.yaml nsynth
python 2pass_lineareval.py config/ast.yaml vc1

(AST-Fusion#5#12)
python 2pass_lineareval.py config/ast_fusion.yaml cremad +name=AR_AST_Fusion512
python 2pass_lineareval.py config/ast_fusion.yaml voxforge +name=AR_AST_Fusion512
python 2pass_lineareval.py config/ast_fusion.yaml esc50 +name=AR_AST_Fusion512
python 2pass_lineareval.py config/ast_fusion.yaml gtzan batch_size=4,+name=AR_AST_Fusion512
python 2pass_lineareval.py config/ast_fusion.yaml spcv2 +name=AR_AST_Fusion512
python 2pass_lineareval.py config/ast_fusion.yaml us8k +name=AR_AST_Fusion512
python 2pass_lineareval.py config/ast_fusion.yaml surge --lr=0.0001 +name=AR_AST_Fusion512
python 2pass_lineareval.py config/ast_fusion.yaml nsynth +name=AR_AST_Fusion512
python 2pass_lineareval.py config/ast_fusion.yaml vc1 batch_size=64,+name=AR_AST_Fusion512

(For probing layer performances)
python 2pass_lineareval.py config/ast_fusion.yaml cremad +name=AR_AST_L1,ast_layers=1
python 2pass_lineareval.py config/ast_fusion.yaml cremad +name=AR_AST_L2,ast_layers=2
python 2pass_lineareval.py config/ast_fusion.yaml cremad +name=AR_AST_L3,ast_layers=3
python 2pass_lineareval.py config/ast_fusion.yaml cremad +name=AR_AST_L4,ast_layers=4
python 2pass_lineareval.py config/ast_fusion.yaml cremad +name=AR_AST_L5,ast_layers=5
python 2pass_lineareval.py config/ast_fusion.yaml cremad +name=AR_AST_L6,ast_layers=6
python 2pass_lineareval.py config/ast_fusion.yaml cremad +name=AR_AST_L7,ast_layers=7
python 2pass_lineareval.py config/ast_fusion.yaml cremad +name=AR_AST_L8,ast_layers=8
python 2pass_lineareval.py config/ast_fusion.yaml cremad +name=AR_AST_L9,ast_layers=9
python 2pass_lineareval.py config/ast_fusion.yaml cremad +name=AR_AST_L10,ast_layers=10
python 2pass_lineareval.py config/ast_fusion.yaml cremad +name=AR_AST_L11,ast_layers=11
python 2pass_lineareval.py config/ast_fusion.yaml voxforge +name=AR_AST_L1,ast_layers=1
python 2pass_lineareval.py config/ast_fusion.yaml voxforge +name=AR_AST_L2,ast_layers=2
python 2pass_lineareval.py config/ast_fusion.yaml voxforge +name=AR_AST_L3,ast_layers=3
python 2pass_lineareval.py config/ast_fusion.yaml voxforge +name=AR_AST_L4,ast_layers=4
python 2pass_lineareval.py config/ast_fusion.yaml voxforge +name=AR_AST_L5,ast_layers=5
python 2pass_lineareval.py config/ast_fusion.yaml voxforge +name=AR_AST_L6,ast_layers=6
python 2pass_lineareval.py config/ast_fusion.yaml voxforge +name=AR_AST_L7,ast_layers=7
python 2pass_lineareval.py config/ast_fusion.yaml voxforge +name=AR_AST_L8,ast_layers=8
python 2pass_lineareval.py config/ast_fusion.yaml voxforge +name=AR_AST_L9,ast_layers=9
python 2pass_lineareval.py config/ast_fusion.yaml voxforge +name=AR_AST_L10,ast_layers=10
python 2pass_lineareval.py config/ast_fusion.yaml voxforge +name=AR_AST_L11,ast_layers=11
python 2pass_lineareval.py config/ast_fusion.yaml esc50 +name=AR_AST_L1,ast_layers=1
python 2pass_lineareval.py config/ast_fusion.yaml esc50 +name=AR_AST_L2,ast_layers=2
python 2pass_lineareval.py config/ast_fusion.yaml esc50 +name=AR_AST_L3,ast_layers=3
python 2pass_lineareval.py config/ast_fusion.yaml esc50 +name=AR_AST_L4,ast_layers=4
python 2pass_lineareval.py config/ast_fusion.yaml esc50 +name=AR_AST_L5,ast_layers=5
python 2pass_lineareval.py config/ast_fusion.yaml esc50 +name=AR_AST_L6,ast_layers=6
python 2pass_lineareval.py config/ast_fusion.yaml esc50 +name=AR_AST_L7,ast_layers=7
python 2pass_lineareval.py config/ast_fusion.yaml esc50 +name=AR_AST_L8,ast_layers=8
python 2pass_lineareval.py config/ast_fusion.yaml esc50 +name=AR_AST_L9,ast_layers=9
python 2pass_lineareval.py config/ast_fusion.yaml esc50 +name=AR_AST_L10,ast_layers=10
python 2pass_lineareval.py config/ast_fusion.yaml esc50 +name=AR_AST_L11,ast_layers=11
python 2pass_lineareval.py config/ast_fusion.yaml gtzan batch_size=12,+name=AR_AST_L1,ast_layers=1
python 2pass_lineareval.py config/ast_fusion.yaml gtzan batch_size=12,+name=AR_AST_L2,ast_layers=2
python 2pass_lineareval.py config/ast_fusion.yaml gtzan batch_size=12,+name=AR_AST_L3,ast_layers=3
python 2pass_lineareval.py config/ast_fusion.yaml gtzan batch_size=12,+name=AR_AST_L4,ast_layers=4
python 2pass_lineareval.py config/ast_fusion.yaml gtzan batch_size=12,+name=AR_AST_L5,ast_layers=5
python 2pass_lineareval.py config/ast_fusion.yaml gtzan batch_size=12,+name=AR_AST_L6,ast_layers=6
python 2pass_lineareval.py config/ast_fusion.yaml gtzan batch_size=12,+name=AR_AST_L7,ast_layers=7
python 2pass_lineareval.py config/ast_fusion.yaml gtzan batch_size=12,+name=AR_AST_L8,ast_layers=8
python 2pass_lineareval.py config/ast_fusion.yaml gtzan batch_size=12,+name=AR_AST_L9,ast_layers=9
python 2pass_lineareval.py config/ast_fusion.yaml gtzan batch_size=12,+name=AR_AST_L10,ast_layers=10
python 2pass_lineareval.py config/ast_fusion.yaml gtzan batch_size=12,+name=AR_AST_L11,ast_layers=11
python 2pass_lineareval.py config/ast_fusion.yaml spcv2 +name=AR_AST_L1,ast_layers=1
python 2pass_lineareval.py config/ast_fusion.yaml spcv2 +name=AR_AST_L2,ast_layers=2
python 2pass_lineareval.py config/ast_fusion.yaml spcv2 +name=AR_AST_L3,ast_layers=3
python 2pass_lineareval.py config/ast_fusion.yaml spcv2 +name=AR_AST_L4,ast_layers=4
python 2pass_lineareval.py config/ast_fusion.yaml spcv2 +name=AR_AST_L5,ast_layers=5
python 2pass_lineareval.py config/ast_fusion.yaml spcv2 +name=AR_AST_L6,ast_layers=6
python 2pass_lineareval.py config/ast_fusion.yaml spcv2 +name=AR_AST_L7,ast_layers=7
python 2pass_lineareval.py config/ast_fusion.yaml spcv2 +name=AR_AST_L8,ast_layers=8
python 2pass_lineareval.py config/ast_fusion.yaml spcv2 +name=AR_AST_L9,ast_layers=9
python 2pass_lineareval.py config/ast_fusion.yaml spcv2 +name=AR_AST_L10,ast_layers=10
python 2pass_lineareval.py config/ast_fusion.yaml spcv2 +name=AR_AST_L11,ast_layers=11
python 2pass_lineareval.py config/ast_fusion.yaml us8k +name=AR_AST_L1,ast_layers=1
python 2pass_lineareval.py config/ast_fusion.yaml us8k +name=AR_AST_L2,ast_layers=2
python 2pass_lineareval.py config/ast_fusion.yaml us8k +name=AR_AST_L3,ast_layers=3
python 2pass_lineareval.py config/ast_fusion.yaml us8k +name=AR_AST_L4,ast_layers=4
python 2pass_lineareval.py config/ast_fusion.yaml us8k +name=AR_AST_L5,ast_layers=5
python 2pass_lineareval.py config/ast_fusion.yaml us8k +name=AR_AST_L6,ast_layers=6
python 2pass_lineareval.py config/ast_fusion.yaml us8k +name=AR_AST_L7,ast_layers=7
python 2pass_lineareval.py config/ast_fusion.yaml us8k +name=AR_AST_L8,ast_layers=8
python 2pass_lineareval.py config/ast_fusion.yaml us8k +name=AR_AST_L9,ast_layers=9
python 2pass_lineareval.py config/ast_fusion.yaml us8k +name=AR_AST_L10,ast_layers=10
python 2pass_lineareval.py config/ast_fusion.yaml us8k +name=AR_AST_L11,ast_layers=11
python 2pass_lineareval.py config/ast_fusion.yaml surge --lr=0.0001 +name=AR_AST_L1,ast_layers=1
python 2pass_lineareval.py config/ast_fusion.yaml surge --lr=0.0001 +name=AR_AST_L2,ast_layers=2
python 2pass_lineareval.py config/ast_fusion.yaml surge --lr=0.0001 +name=AR_AST_L3,ast_layers=3
python 2pass_lineareval.py config/ast_fusion.yaml surge --lr=0.0001 +name=AR_AST_L4,ast_layers=4
python 2pass_lineareval.py config/ast_fusion.yaml surge --lr=0.0001 +name=AR_AST_L5,ast_layers=5
python 2pass_lineareval.py config/ast_fusion.yaml surge --lr=0.0001 +name=AR_AST_L6,ast_layers=6
python 2pass_lineareval.py config/ast_fusion.yaml surge --lr=0.0001 +name=AR_AST_L7,ast_layers=7
python 2pass_lineareval.py config/ast_fusion.yaml surge --lr=0.0001 +name=AR_AST_L8,ast_layers=8
python 2pass_lineareval.py config/ast_fusion.yaml surge --lr=0.0001 +name=AR_AST_L9,ast_layers=9
python 2pass_lineareval.py config/ast_fusion.yaml surge --lr=0.0001 +name=AR_AST_L10,ast_layers=10
python 2pass_lineareval.py config/ast_fusion.yaml surge --lr=0.0001 +name=AR_AST_L11,ast_layers=11
python 2pass_lineareval.py config/ast_fusion.yaml nsynth +name=AR_AST_L1,ast_layers=1
python 2pass_lineareval.py config/ast_fusion.yaml nsynth +name=AR_AST_L2,ast_layers=2
python 2pass_lineareval.py config/ast_fusion.yaml nsynth +name=AR_AST_L3,ast_layers=3
python 2pass_lineareval.py config/ast_fusion.yaml nsynth +name=AR_AST_L4,ast_layers=4
python 2pass_lineareval.py config/ast_fusion.yaml nsynth +name=AR_AST_L5,ast_layers=5
python 2pass_lineareval.py config/ast_fusion.yaml nsynth +name=AR_AST_L6,ast_layers=6
python 2pass_lineareval.py config/ast_fusion.yaml nsynth +name=AR_AST_L7,ast_layers=7
python 2pass_lineareval.py config/ast_fusion.yaml nsynth +name=AR_AST_L8,ast_layers=8
python 2pass_lineareval.py config/ast_fusion.yaml nsynth +name=AR_AST_L9,ast_layers=9
python 2pass_lineareval.py config/ast_fusion.yaml nsynth +name=AR_AST_L10,ast_layers=10
python 2pass_lineareval.py config/ast_fusion.yaml nsynth +name=AR_AST_L11,ast_layers=11
python 2pass_lineareval.py config/ast_fusion.yaml vc1 +name=AR_AST_L1,ast_layers=1
python 2pass_lineareval.py config/ast_fusion.yaml vc1 +name=AR_AST_L2,ast_layers=2
python 2pass_lineareval.py config/ast_fusion.yaml vc1 +name=AR_AST_L3,ast_layers=3
python 2pass_lineareval.py config/ast_fusion.yaml vc1 +name=AR_AST_L4,ast_layers=4
python 2pass_lineareval.py config/ast_fusion.yaml vc1 +name=AR_AST_L5,ast_layers=5
python 2pass_lineareval.py config/ast_fusion.yaml vc1 +name=AR_AST_L6,ast_layers=6
python 2pass_lineareval.py config/ast_fusion.yaml vc1 +name=AR_AST_L7,ast_layers=7
python 2pass_lineareval.py config/ast_fusion.yaml vc1 +name=AR_AST_L8,ast_layers=8
python 2pass_lineareval.py config/ast_fusion.yaml vc1 +name=AR_AST_L9,ast_layers=9
python 2pass_lineareval.py config/ast_fusion.yaml vc1 +name=AR_AST_L10,ast_layers=10
python 2pass_lineareval.py config/ast_fusion.yaml vc1 +name=AR_AST_L11,ast_layers=11
```

# BYOL-A

```sh
python 2pass_lineareval.py config/byola.yaml spcv2
python 2pass_lineareval.py config/byola.yaml us8k
python 2pass_lineareval.py config/byola.yaml surge --lr=0.0001
python 2pass_lineareval.py config/byola.yaml nsynth
python 2pass_lineareval.py config/byola.yaml vc1
python 2pass_lineareval.py config/byola.yaml cremad
python 2pass_lineareval.py config/byola.yaml voxforge
python 2pass_lineareval.py config/byola.yaml esc50
python 2pass_lineareval.py config/byola.yaml gtzan batch_size=128 --lr=0.001
```
