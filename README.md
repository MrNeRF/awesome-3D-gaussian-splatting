# Awesome 3D Gaussian Splatting Resources 

A curated list of papers and resources focused on 3D Gaussian Splatting, intended to keep pace with the anticipated surge of research in the coming months. If you have any additions or suggestions, feel free to contribute. Additional resources like blog posts, videos, etc. are also welcome.

### Update Log:
- **October 15, 2023**: Initial list with first 6 papers.

## Seminal Paper Introducing 3D Gaussian Splatting
### 3D Gaussian Splatting for Real-Time Radiance Field Rendering
- **Authors**: Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis
- **Abstract**: Radiance Field methods have recently revolutionized novel-view synthesis... (shortened for readability)
  
  [📄 Paper (Low Resolution)](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/3d_gaussian_splatting_low.pdf) | [📄 Paper (High Resolution)](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/3d_gaussian_splatting_high.pdf) | [🌐 Project Page](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) | [💻 Code](https://github.com/graphdeco-inria/gaussian-splatting) | [🎥 Short Presentation](https://youtu.be/T_kXY43VZnk?si=DrkbDFxQAv5scQNT) | [🎥 Explanation Video](https://www.youtube.com/live/xgwvU7S0K-k?si=edF8NkYtsRbgTbKi)

## Dynamic 3D Gaussian Splatting

### 1. Dynamic 3D Gaussians: Tracking by Persistent Dynamic View Synthesis
- **Authors**: Jonathon Luiten, Georgios Kopanas, Bastian Leibe, Deva Ramanan
- **Abstract**: Radiance Field methods have recently revolutionized novel-view synthesis
of scenes captured with multiple photos or videos. However, achieving high visual quality still requires neural networks that are costly to train and render, while recent faster methods inevitably trade off speed for quality... (shortened for readability)

  [📄 Paper](https://dynamic3dgaussians.github.io/paper.pdf) | [🌐 Project Page](https://dynamic3dgaussians.github.io/) | [💻 Code](https://github.com/JonathonLuiten/Dynamic3DGaussians) | [🎥 Explanation Video](https://www.youtube.com/live/hDuy1TgD8I4?si=6oGN0IYnPRxOibpg)

### 2. 4D Gaussian Splatting for Real-Time Dynamic Scene Rendering
- **Authors**: Guanjun Wu, Taoran Yi, Jiemin Fang, Lingxi Xie, Xiaopeng Zhang, Wei Wei, Wenyu Liu, Tian Qi, Xinggang Wang
- **Abstract**: Representing and rendering dynamic scenes has been an important but challenging task. Especially, to accurately model complex motions, high efficiency is usually hard to maintain. We introduce the 4D Gaussian Splatting (4D-GS) to achieve real-time dynamic scene rendering... (shortened for readability)

  [📄 Paper](https://arxiv.org/pdf/2310.08528.pdf) | [🌐 Project Page](https://guanjunwu.github.io/4dgs/) | [💻 Code](https://github.com/hustvl/4DGaussians)
  
## Diffusion 3D Gaussian Splatting

### 1. DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content Creation
- **Authors**: Jiaxiang Tang, Jiawei Ren, Hang Zhou, Ziwei Liu, Gang Zeng
- **Abstract**: Recent advances in 3D content creation mostly leverage optimization-based 3D
generation via score distillation sampling (SDS). Though promising results have
been exhibited, these methods often suffer from slow per-sample optimization,
limiting their practical usage.... (shortened for readability)

  [📄 Paper](https://arxiv.org/pdf/2309.16653.pdf) | [🌐 Project Page](https://dreamgaussian.github.io/) | [💻 Code](https://github.com/dreamgaussian/dreamgaussian) | [🎥 Explanation Video](https://www.youtube.com/live/l956ye13F8M?si=ZkvFL_lsY5OQUB7e)

### 2. Text-to-3D using Gaussian Splatting
- **Authors**: Zilong Chen, Feng Wang, Huaping Liu
- **Abstract**: In this paper, we present Gaussian Splatting based text-to-3D generation (GSGEN),
a novel approach for generating high-quality 3D objects. Previous methods suffer
from inaccurate geometry and limited fidelity due to the absence of 3D prior and
proper representation... (shortened for readability)

  [📄 Paper](https://arxiv.org/pdf/2309.16585.pdf) | [🌐 Project Page](https://gsgen3d.github.io/) | [💻 Code](https://github.com/gsgen3d/gsgen) | [🎥 Short Presentation](https://streamable.com/28snte) |  [🎥 Explanation Video](https://www.youtube.com/live/l956ye13F8M?si=ZkvFL_lsY5OQUB7e)

### 3. GaussianDreamer: Fast Generation from Text to 3D Gaussian Splatting with Point Cloud Priors
- **Authors**:  Taoran Yi1, Jiemin Fang, Guanjun Wu1, Lingxi Xie, Xiaopeng Zhang,
Wenyu Liu, Tian Qi, Xinggang Wang 
- **Abstract**: In recent times, the generation of 3D assets from text prompts has shown impressive results. Both 2D and 3D diffusion models can generate decent 3D objects based on prompts. 3D diffusion models have good 3D consistency, but their quality and generalization are limited as trainable 3D data is expensive and hard to obtain.... (shortened for readability)

  [📄 Paper](https://arxiv.org/pdf/2310.08529.pdf) | [🌐 Project Page](https://taoranyi.com/gaussiandreamer/) | [💻 Code (to be released)](https://github.com/hustvl/GaussianDreamer) 

## Credits