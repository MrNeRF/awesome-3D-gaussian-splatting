# Awesome 3D Gaussian Splatting Resources 

A curated list of papers and open source resources focused on 3D Gaussian Splatting, intended to keep pace with the anticipated surge of research in the coming months. If you have any additions or suggestions, feel free to contribute. Additional resources like blog posts, videos, etc. are also welcome.

### Update Log:
- **October 18, 2023**: 
  - Added Github page link for Real-time Photorealistic Dynamic Scene Representation.
  - Re-ordered headings.
  - Added other unofficial implementations of the method.
  - Moved Nerfstudio gplat to Unofficial Implementations.
  - Added Nerfstudio, Blender, WebRTC, iOS & Metal and Unreal viewers.
- **October 17, 2023**: 
  - GaussianDreamer code released.
  - Added Real-time Photorealistic Dynamic Scene Representation.
- **October 16, 2023**: 
  - Added Deformable 3D Gaussians paper.
  - Dynamic 3D Gaussians code released.
- **October 15, 2023**: Initial list with first 6 papers.

## Seminal Paper introducing 3D Gaussian Splatting:
### 3D Gaussian Splatting for Real-Time Radiance Field Rendering
**Authors**: Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis

<details open>
<summary><b>Abstract</b></summary>
Radiance Field methods have recently revolutionized novel-view synthesis
of scenes captured with multiple photos or videos. However, achieving high
visual quality still requires neural networks that are costly to train and ren-
der, while recent faster methods inevitably trade off speed for quality. For
unbounded and complete scenes (rather than isolated objects) and 1080p
resolution rendering, no current method can achieve real-time display rates.
We introduce three key elements that allow us to achieve state-of-the-art
visual quality while maintaining competitive training times and importantly
allow high-quality real-time (≥ 30 fps) novel-view synthesis at 1080p resolu-
tion. First, starting from sparse points produced during camera calibration,
we represent the scene with 3D Gaussians that preserve desirable proper-
ties of continuous volumetric radiance fields for scene optimization while
avoiding unnecessary computation in empty space; Second, we perform
interleaved optimization/density control of the 3D Gaussians, notably opti-
mizing anisotropic covariance to achieve an accurate representation of the
scene; Third, we develop a fast visibility-aware rendering algorithm that
supports anisotropic splatting and both accelerates training and allows real-
time rendering. We demonstrate state-of-the-art visual quality and real-time
rendering on several established datasets.
</details>
  
  [📄 Paper (Low Resolution)](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/3d_gaussian_splatting_low.pdf) | [📄 Paper (High Resolution)](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/3d_gaussian_splatting_high.pdf) | [🌐 Project Page](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) | [💻 Code](https://github.com/graphdeco-inria/gaussian-splatting) | [🎥 Short Presentation](https://youtu.be/T_kXY43VZnk?si=DrkbDFxQAv5scQNT) | [🎥 Explanation Video](https://www.youtube.com/live/xgwvU7S0K-k?si=edF8NkYtsRbgTbKi)

## Dynamic 3D Gaussian Splatting:
### 1. Dynamic 3D Gaussians: Tracking by Persistent Dynamic View Synthesis
**Authors**: Jonathon Luiten, Georgios Kopanas, Bastian Leibe, Deva Ramanan

<details open>
<summary><b>Abstract</b></summary>
We present a method that simultaneously addresses the
tasks of dynamic scene novel-view synthesis and six degree-
of-freedom (6-DOF) tracking of all dense scene elements.
We follow an analysis-by-synthesis framework, inspired by
recent work that models scenes as a collection of 3D Gaus-
sians which are optimized to reconstruct input images via
differentiable rendering. To model dynamic scenes, we al-
low Gaussians to move and rotate over time while enforcing
that they have persistent color, opacity, and size. By regu-
larizing Gaussians’ motion and rotation with local-rigidity
constraints, we show that our Dynamic 3D Gaussians cor-
rectly model the same area of physical space over time, in-
cluding the rotation of that space. Dense 6-DOF tracking
and dynamic reconstruction emerges naturally from persis-
tent dynamic view synthesis, without requiring any corre-
spondence or flow as input. We demonstrate a large num-
ber of downstream applications enabled by our representa-
tion, including first-person view synthesis, dynamic compo-
sitional scene synthesis, and 4D video editing.
</details>

  [📄 Paper](https://dynamic3dgaussians.github.io/paper.pdf) | [🌐 Project Page](https://dynamic3dgaussians.github.io/) | [💻 Code](https://github.com/JonathonLuiten/Dynamic3DGaussians) | [🎥 Explanation Video](https://www.youtube.com/live/hDuy1TgD8I4?si=6oGN0IYnPRxOibpg)

### 2. Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction
**Authors**: Ziyi Yang, Xinyu Gao, Wen Zhou, Shaohui Jiao, Yuqing Zhang, Xiaogang Jin 

<details open>
<summary><b>Abstract</b></summary>
Implicit neural representation has opened up new avenues for dynamic scene reconstruction and rendering. Nonetheless, state-of-the-art methods of dynamic neural rendering rely heavily on these implicit representations, which frequently struggle with accurately capturing the intricate details of objects in the scene. Furthermore, implicit methods struggle to achieve real-time rendering in general dynamic scenes, limiting their use in a wide range of tasks. To address the issues, we propose a deformable 3D Gaussians Splatting method that reconstructs scenes using explicit 3D Gaussians and learns Gaussians in canonical space with a deformation field to model monocular dynamic scenes. We also introduced a smoothing training mechanism with no extra overhead to mitigate the impact of inaccurate poses in real datasets on the smoothness of time interpolation tasks. Through differential gaussian rasterization, the deformable 3D Gaussians not only achieve higher rendering quality but also real-time rendering speed. Experiments show that our method outperforms existing methods significantly in terms of both rendering quality and speed, making it well-suited for tasks such as novel-view synthesis, time synthesis, and real-time rendering. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2309.13101.pdf) | [🌐 Project Page](https://ingra14m.github.io/Deformable-Gaussians/) | [💻 Code (to be released)](https://github.com/ingra14m/Deformable-3D-Gaussians) 

### 3. 4D Gaussian Splatting for Real-Time Dynamic Scene Rendering
**Authors**: Guanjun Wu, Taoran Yi, Jiemin Fang, Lingxi Xie, Xiaopeng Zhang, Wei Wei, Wenyu Liu, Tian Qi, Xinggang Wang

<details open>
<summary><b>Abstract</b></summary>
Representing and rendering dynamic scenes has been an
important but challenging task. Especially, to accurately
model complex motions, high efficiency is usually hard to
maintain. We introduce the 4D Gaussian Splatting (4D-GS)
to achieve real-time dynamic scene rendering while also
enjoying high training and storage efficiency. An efficient
deformation field is constructed to model both Gaussian
motions and shape deformations. Different adjacent Gaus-
sians are connected via a HexPlane to produce more accu-
rate position and shape deformations. Our 4D-GS method
achieves real-time rendering under high resolutions, 70
FPS at a 800×800 resolution on an RTX 3090 GPU, while
maintaining comparable or higher quality than previous
state-of-the-art method.
</details>

  [📄 Paper](https://arxiv.org/pdf/2310.08528.pdf) | [🌐 Project Page](https://guanjunwu.github.io/4dgs/) | [💻 Code](https://github.com/hustvl/4DGaussians)
  
### 4. Real-time Photorealistic Dynamic Scene Representation and Rendering with 4D Gaussian Splatting

<details open>
<summary><b>Abstract</b></summary>
Reconstructing dynamic 3D scenes from 2D images and generating diverse views over time is challenging due to scene complexity and temporal dynamics. Despite advancements in neural implicit models, limitations persist: (i) Inadequate Scene Structure: Existing methods struggle to reveal the spatial and temporal structure of dynamic scenes from directly learning the complex 6D plenoptic function. (ii) Scaling Deformation Modeling: Explicitly modeling scene element deformation becomes impractical for complex dynamics. To address these issues, we consider the spacetime as an entirety and propose to approximate the underlying spatio-temporal 4D volume of a dynamic scene by optimizing a collection of 4D primitives, with explicit geometry and appearance modeling. Learning to optimize the 4D primitives enables us to synthesize novel views at any desired time with our tailored rendering routine. Our model is conceptually simple, consisting of a 4D Gaussian parameterized by anisotropic ellipses that can rotate arbitrarily in space and time, as well as view-dependent and time-evolved appearance represented by the coefficient of 4D spherindrical harmonics. This approach offers simplicity, flexibility for variable-length video and end-to-end training, and efficient real-time rendering, making it suitable for capturing complex dynamic scene motions. Experiments across various benchmarks, including monocular and multi-view scenarios, demonstrate our 4DGS model's superior visual quality and efficiency. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2310.10642.pdf) | [💻 Code (to be released)](https://github.com/fudan-zvg/4d-gaussian-splatting) 

## Diffusion 3D Gaussian Splatting:

### 1. Text-to-3D using Gaussian Splatting
**Authors**: Zilong Chen, Feng Wang, Huaping Liu

<details open>
<summary><b>Abstract</b></summary>
In this paper, we present Gaussian Splatting based text-to-3D generation (GSGEN),
a novel approach for generating high-quality 3D objects. Previous methods suffer
from inaccurate geometry and limited fidelity due to the absence of 3D prior and
proper representation. We leverage 3D Gaussian Splatting, a recent state-of-the-art
representation, to address existing shortcomings by exploiting the explicit nature
that enables the incorporation of 3D prior. Specifically, our method adopts a pro-
gressive optimization strategy, which includes a geometry optimization stage and an
appearance refinement stage. In geometry optimization, a coarse representation is
established under a 3D geometry prior along with the ordinary 2D SDS loss, ensur-
ing a sensible and 3D-consistent rough shape. Subsequently, the obtained Gaussians
undergo an iterative refinement to enrich details. In this stage, we increase the num-
ber of Gaussians by compactness-based densification to enhance continuity and
improve fidelity. With these designs, our approach can generate 3D content with
delicate details and more accurate geometry. Extensive evaluations demonstrate the
effectiveness of our method, especially for capturing high-frequency components.
</details>

[📄 Paper](https://arxiv.org/pdf/2309.16585.pdf) | [🌐 Project Page](https://gsgen3d.github.io/) | [💻 Code](https://github.com/gsgen3d/gsgen) | [🎥 Short Presentation](https://streamable.com/28snte) | [🎥 Explanation Video](https://www.youtube.com/live/l956ye13F8M?si=ZkvFL_lsY5OQUB7e)


### 2. DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content Creation
**Authors**: Jiaxiang Tang, Jiawei Ren, Hang Zhou, Ziwei Liu, Gang Zeng

<details open>
<summary><b>Abstract</b></summary>
Recent advances in 3D content creation mostly leverage optimization-based 3D
generation via score distillation sampling (SDS). Though promising results have
been exhibited, these methods often suffer from slow per-sample optimization,
limiting their practical usage. In this paper, we propose DreamGaussian, a novel
3D content generation framework that achieves both efficiency and quality simul-
taneously. Our key insight is to design a generative 3D Gaussian Splatting model
with companioned mesh extraction and texture refinement in UV space. In con-
trast to the occupancy pruning used in Neural Radiance Fields, we demonstrate
that the progressive densification of 3D Gaussians converges significantly faster
for 3D generative tasks. To further enhance the texture quality and facilitate down-
stream applications, we introduce an efficient algorithm to convert 3D Gaussians
into textured meshes and apply a fine-tuning stage to refine the details. Exten-
sive experiments demonstrate the superior efficiency and competitive generation
quality of our proposed approach. Notably, DreamGaussian produces high-quality
textured meshes in just 2 minutes from a single-view image, achieving approxi-
mately 10 times acceleration compared to existing methods.
</details>

  [📄 Paper](https://arxiv.org/pdf/2309.16653.pdf) | [🌐 Project Page](https://dreamgaussian.github.io/) | [💻 Code](https://github.com/dreamgaussian/dreamgaussian) | [🎥 Explanation Video](https://www.youtube.com/live/l956ye13F8M?si=ZkvFL_lsY5OQUB7e)

### 3. GaussianDreamer: Fast Generation from Text to 3D Gaussian Splatting with Point Cloud Priors
**Authors**:  Taoran Yi1, Jiemin Fang, Guanjun Wu1, Lingxi Xie, Xiaopeng Zhang,
Wenyu Liu, Tian Qi, Xinggang Wang 
<details open>
<summary><b>Abstract</b></summary>
In recent times, the generation of 3D assets from text
prompts has shown impressive results. Both 2D and 3D
diffusion models can generate decent 3D objects based on
prompts. 3D diffusion models have good 3D consistency,
but their quality and generalization are limited as trainable 
3D data is expensive and hard to obtain. 2D diffusion models enjoy strong abilities of generalization and
fine generation, but the 3D consistency is hard to guarantee. This paper attempts to bridge the power from the two
types of diffusion models via the recent explicit and efficient
3D Gaussian splatting representation. A fast 3D generation framework, named as GaussianDreamer, is proposed,
where the 3D diffusion model provides point cloud priors
for initialization and the 2D diffusion model enriches the
geometry and appearance. Operations of noisy point growing and color perturbation are introduced to enhance the
initialized Gaussians. Our GaussianDreamer can generate a high-quality 3D instance within 25 minutes on one
GPU, much faster than previous methods, while the generated instances can be directly rendered in real time.
</details>

  [📄 Paper](https://arxiv.org/pdf/2310.08529.pdf) | [🌐 Project Page](https://taoranyi.com/gaussiandreamer/) | [💻 Code](https://github.com/hustvl/GaussianDreamer) 

## Open Source Implementations 

### Reference 
- [Gaussian Splatting](https://github.com/graphdeco-inria/gaussian-splatting)

### Training
- [fast: C++/CUDA](https://github.com/MrNeRF/gaussian-splatting-cuda)
  
### Unofficial Implementations
- [Taichi 3D Gaussian Splatting](https://github.com/wanmeihuali/taichi_3d_gaussian_splatting)
- [Gaussian Splatting 3D](https://github.com/heheyas/gaussian_splatting_3d)
- [3D Gaussian Splatting](https://github.com/WangFeng18/3d-gaussian-splatting)
- [nerfstudio: python/CUDA](https://github.com/nerfstudio-project/gsplat)

### Game Engines 
- [Unity Implementation](https://github.com/aras-p/UnityGaussianSplatting)

### Viewers
- [WebGL Viewer 1](https://github.com/antimatter15/splat)
- [WebGL Viewer 2](https://github.com/cvlab-epfl/gaussian-splatting-web)
- [Three.js](https://github.com/mkkellogg/GaussianSplats3D)
- [A-Frame](https://github.com/quadjr/aframe-gaussian-splatting)
- [Nerfstudio Unofficial](https://github.com/yzslab/nerfstudio/tree/gaussian_splatting)
- [Nerfstudio Viser](https://github.com/nerfstudio-project/viser)
- [Blender (Editor)](https://github.com/ReshotAI/gaussian-splatting-blender-addon/tree/master)
- [WebRTC viewer](https://github.com/dylanebert/gaussian-viewer)
- [iOS & Metal viewer](https://github.com/laanlabs/metal-splats)
- [Unreal via Volinga](https://volinga.ai/)

## Blog Posts

1. [Gaussian Splatting is pretty cool](https://aras-p.info/blog/2023/09/05/Gaussian-Splatting-is-pretty-cool/)
2. [Making Gaussian Splats smaller](https://aras-p.info/blog/2023/09/13/Making-Gaussian-Splats-smaller/)
3. [Making Gaussian Splats more smaller](https://aras-p.info/blog/2023/09/27/Making-Gaussian-Splats-more-smaller/)

## Tutorial Videos

1. [Getting Started with 3DGS](https://youtu.be/UXtuigy_wYc?si=j1vfORNspcocSH-b)
2. [How to view 3DGS Scenes in Unity](https://youtu.be/5_GaPYBHqOo?si=6u9j1HqXwF_5WSUL)

## Credits

Thanks to [leonidk](https://github.com/leonidk) for informing me about the release of the paper "Real-time Photorealistic Dynamic Scene Representation and Rendering with 4D Gaussian Splatting".
