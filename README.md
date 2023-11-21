# Awesome 3D Gaussian Splatting Resources 

A curated list of papers and open-source resources focused on 3D Gaussian Splatting, intended to keep pace with the anticipated surge of research in the coming months. If you have any additions or suggestions, feel free to contribute. Additional resources like blog posts, videos, etc. are also welcome.

<details span>
<summary><b>Update Log:</b></summary>
<br>

 **November 21, 2023**:
  - Added the paper GS-SLAM

**November 17, 2023**:
  - Added PlayCanvas implementation to Game Engines section.

 **November 16, 2023**:
  - Deformable 3D Gaussians code released.
  - Drivable 3D Gaussian Avatars paper added. 

 **November 8, 2023**:
  - Some notes about the 3DGS implementation and unsiversal format discussion.

 **November 4, 2023**:
  - Added 2D gaussian splatting.
  - Added very detailed (technical) blog post explaining 3D gaussian splatting.

 **October 28, 2023**:
  - Added Utilities Section.
  - Added 3DGS Converter for editing 3DGS .ply files in Cloud Compare to Utilities.
  - Added Kapture (for bundler to colmap model conversion) and Kapture image cropper script with conversion instructions to Utilities.

 **October 23, 2023**:
  - Added python WebGL viewer 2.
  - Added Intro to gaussian splatting (and Unity viewer) video blog.

  **October 21, 2023**:
  - Added python OpenGL viewer.
  - Added typescript WebGPU viewer.

  **October 20, 2023**:
  - Made abstracts readable (removed hyphenations).
  - Added Windows tutorial.
  - Other minor text fixes.
  - Added Jupyter notebook viewer.

**October 19, 2023**: 
  - Added Github page link for Real-time Photorealistic Dynamic Scene Representation.
  - Re-ordered headings.
  - Added other unofficial implementations.
  - Moved Nerfstudio gsplat and fast: C++/CUDA to Unofficial Implementations.
  - Added Nerfstudio, Blender, WebRTC, iOS & Metal viewers.

**October 17, 2023**: 
  - GaussianDreamer code released.
  - Added Real-time Photorealistic Dynamic Scene Representation.

**October 16, 2023**: 
  - Added Deformable 3D Gaussians paper.
  - Dynamic 3D Gaussians code released.
**October 15, 2023**: Initial list with first 6 papers.
</details>

## Seminal Paper introducing 3D Gaussian Splatting:
### 3D Gaussian Splatting for Real-Time Radiance Field Rendering
**Authors**: Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis

<details open>
<summary><b>Abstract</b></summary>
Radiance Field methods have recently revolutionized novel-view synthesis
of scenes captured with multiple photos or videos. However, achieving high
visual quality still requires neural networks that are costly to train and render,
while recent faster methods inevitably trade off speed for quality. For
unbounded and complete scenes (rather than isolated objects) and 1080p
resolution rendering, no current method can achieve real-time display rates.
We introduce three key elements that allow us to achieve state-of-the-art
visual quality while maintaining competitive training times and importantly
allow high-quality real-time (≥ 30 fps) novel-view synthesis at 1080p resolution.
First, starting from sparse points produced during camera calibration,
we represent the scene with 3D Gaussians that preserve desirable properties
of continuous volumetric radiance fields for scene optimization while
avoiding unnecessary computation in empty space; Second, we perform
interleaved optimization/density control of the 3D Gaussians, notably optimizing
anisotropic covariance to achieve an accurate representation of the
scene; Third, we develop a fast visibility-aware rendering algorithm that
supports anisotropic splatting and both accelerates training and allows real-time
rendering. We demonstrate state-of-the-art visual quality and real-time
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
recent work that models scenes as a collection of 3D Gaussians
which are optimized to reconstruct input images via
differentiable rendering. To model dynamic scenes, we al-
low Gaussians to move and rotate over time while enforcing
that they have persistent color, opacity, and size. By regularizing
Gaussians’ motion and rotation with local-rigidity
constraints, we show that our Dynamic 3D Gaussians correctly
model the same area of physical space over time, including
the rotation of that space. Dense 6-DOF tracking
and dynamic reconstruction emerges naturally from persistent
dynamic view synthesis, without requiring any correspondence
or flow as input. We demonstrate a large number of
downstream applications enabled by our representation,
including first-person view synthesis, dynamic compositional
scene synthesis, and 4D video editing.
</details>

  [📄 Paper](https://dynamic3dgaussians.github.io/paper.pdf) | [🌐 Project Page](https://dynamic3dgaussians.github.io/) | [💻 Code](https://github.com/JonathonLuiten/Dynamic3DGaussians) | [🎥 Explanation Video](https://www.youtube.com/live/hDuy1TgD8I4?si=6oGN0IYnPRxOibpg)

### 2. Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction
**Authors**: Ziyi Yang, Xinyu Gao, Wen Zhou, Shaohui Jiao, Yuqing Zhang, Xiaogang Jin 

<details open>
<summary><b>Abstract</b></summary>
Implicit neural representation has opened up new avenues for dynamic scene reconstruction and rendering. Nonetheless, state-of-the-art methods of dynamic neural rendering rely heavily on these implicit representations, which frequently struggle with accurately capturing the intricate details of objects in the scene. Furthermore, implicit methods struggle to achieve real-time rendering in general dynamic scenes, limiting their use in a wide range of tasks. To address the issues, we propose a deformable 3D Gaussians Splatting method that reconstructs scenes using explicit 3D Gaussians and learns Gaussians in canonical space with a deformation field to model monocular dynamic scenes. We also introduced a smoothing training mechanism with no extra overhead to mitigate the impact of inaccurate poses in real datasets on the smoothness of time interpolation tasks. Through differential gaussian rasterization, the deformable 3D Gaussians not only achieve higher rendering quality but also real-time rendering speed. Experiments show that our method outperforms existing methods significantly in terms of both rendering quality and speed, making it well-suited for tasks such as novel-view synthesis, time synthesis, and real-time rendering. 
</details>

  [📄 Paper](https://arxiv.org/pdf/2309.13101.pdf) | [🌐 Project Page](https://ingra14m.github.io/Deformable-Gaussians/) | [💻 Code](https://github.com/ingra14m/Deformable-3D-Gaussians) 

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
motions and shape deformations. Different adjacent Gaussians
are connected via a HexPlane to produce more accurate
position and shape deformations. Our 4D-GS method
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
established under a 3D geometry prior along with the ordinary 2D SDS loss, ensuring
a sensible and 3D-consistent rough shape. Subsequently, the obtained Gaussians
undergo an iterative refinement to enrich details. In this stage, we increase the number
of Gaussians by compactness-based densification to enhance continuity and
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
3D content generation framework that achieves both efficiency and quality simultaneously.
Our key insight is to design a generative 3D Gaussian Splatting model
with companioned mesh extraction and texture refinement in UV space. In contrast
to the occupancy pruning used in Neural Radiance Fields, we demonstrate
that the progressive densification of 3D Gaussians converges significantly faster
for 3D generative tasks. To further enhance the texture quality and facilitate downstream
applications, we introduce an efficient algorithm to convert 3D Gaussians
into textured meshes and apply a fine-tuning stage to refine the details. Extensive
experiments demonstrate the superior efficiency and competitive generation
quality of our proposed approach. Notably, DreamGaussian produces high-quality
textured meshes in just 2 minutes from a single-view image, achieving approximately
10 times acceleration compared to existing methods.
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

## 3D Gaussian Splatting Avatars:
### 1. Drivable 3D Gaussian Avatars 
**Authors**:  Wojciech Zielonka, Timur Bagautdinov, Shunsuke Saito, Michael Zollhöfer, Justus Thies, Javier Romero
<details open>
<summary><b>Abstract</b></summary>
We present Drivable 3D Gaussian Avatars (D3GA), the
first 3D controllable model for human bodies rendered with
Gaussian splats. Current photorealistic drivable avatars
require either accurate 3D registrations during training,
dense input images during testing, or both. The ones based
on neural radiance fields also tend to be prohibitively slow
for telepresence applications. This work uses the recently
presented 3D Gaussian Splatting (3DGS) technique to render realistic humans at real-time framerates, using dense
calibrated multi-view videos as input. To deform those
primitives, we depart from the commonly used point deformation method of linear blend skinning (LBS) and use
a classic volumetric deformation method: cage deformations. Given their smaller size, we drive these deformations
with joint angles and keypoints, which are more suitable for
communication applications. Our experiments on nine subjects with varied body shapes, clothes, and motions obtain
higher-quality results than state-of-the-art methods when
using the same training and test data.
</details>

  [📄 Paper](https://arxiv.org/pdf/2311.08581.pdf) | [🌐 Project Page](https://zielon.github.io/d3ga/) | | [🎥 Short Presentation](https://youtu.be/C4IT1gnkaF0?si=zUJLm8adM68pVvR8) 

## 3D Gaussian Splatting SLAM:
### 1. GS-SLAM: Dense Visual SLAM with 3D Gaussian Splatting 
**Authors**: Chi Yan, Delin Qu, Dong Wang, Dan Xu, Zhigang Wang, Bin Zhao, Xuelong Li
<details open>
<summary><b>Abstract</b></summary>
In this paper, we introduce GS-SLAM that first utilizes 3D Gaussian representation in the Simultaneous Localization and Mapping (SLAM) system. It facilitates a better balance between efficiency and accuracy. Compared to recent SLAM methods employing neural implicit representations, our method utilizes a real-time differentiable splatting rendering pipeline that offers significant speedup to map optimization and RGB-D re-rendering. Specifically, we propose an adaptive expansion strategy that adds new or deletes noisy 3D Gaussian in order to efficiently reconstruct new observed scene geometry and improve the mapping of previously observed areas. This strategy is essential to extend 3D Gaussian representation to reconstruct the whole scene rather than synthesize a static object in existing methods. Moreover, in the pose tracking process, an effective coarse-to-fine technique is designed to select reliable 3D Gaussian representations to optimize camera pose, resulting in runtime reduction and robust estimation. Our method achieves competitive performance compared with existing state-of-the-art real-time methods on the Replica, TUM-RGBD datasets. The source code will be released upon acceptance. 
</details>

  [📄 Paper](https://arxiv.org/abs/2311.11700) 


## Open Source Implementations 

### Reference 
- [Gaussian Splatting](https://github.com/graphdeco-inria/gaussian-splatting)

### Unofficial Implementations
- [Taichi 3D Gaussian Splatting](https://github.com/wanmeihuali/taichi_3d_gaussian_splatting)
- [Gaussian Splatting 3D](https://github.com/heheyas/gaussian_splatting_3d)
- [3D Gaussian Splatting](https://github.com/WangFeng18/3d-gaussian-splatting)
- [fast: C++/CUDA](https://github.com/MrNeRF/gaussian-splatting-cuda)
- [nerfstudio: python/CUDA](https://github.com/nerfstudio-project/gsplat)

### 2D Gaussian Splatting
- [jupyter notebook 2D GS splatting](https://github.com/OutofAi/2D-Gaussian-Splatting)

### Game Engines 
- [Unity Implementation](https://github.com/aras-p/UnityGaussianSplatting)
- [PlayCanvas Implementation](https://github.com/playcanvas/engine/tree/main/extras/splat)

### Viewers
- [WebGL Viewer 1](https://github.com/antimatter15/splat)
- [WebGL Viewer 2](https://github.com/kishimisu/Gaussian-Splatting-WebGL)
- [WebGPU Viewer 1](https://github.com/cvlab-epfl/gaussian-splatting-web)
- [WebGPU Viewer 2](https://github.com/MarcusAndreasSvensson/gaussian-splatting-webgpu)
- [Three.js](https://github.com/mkkellogg/GaussianSplats3D)
- [A-Frame](https://github.com/quadjr/aframe-gaussian-splatting)
- [Nerfstudio Unofficial](https://github.com/yzslab/nerfstudio/tree/gaussian_splatting)
- [Nerfstudio Viser](https://github.com/nerfstudio-project/viser)
- [Blender (Editor)](https://github.com/ReshotAI/gaussian-splatting-blender-addon/tree/master)
- [WebRTC viewer](https://github.com/dylanebert/gaussian-viewer)
- [iOS & Metal viewer](https://github.com/laanlabs/metal-splats)
- [jupyter notebook](https://github.com/shumash/gaussian-splatting/blob/mshugrina/interactive/interactive.ipynb)
- [python OpenGL viewer](https://github.com/limacv/GaussianSplattingViewer.git)
- [PlayCanvas Viewer](https://github.com/playcanvas/model-viewer)
- [gsplat.js](https://github.com/dylanebert/gsplat.js)

### Utilities
- [Kapture](https://github.com/naver/kapture) - a unified data format to facilitate visual localization and structure from motion e.g. for bundler to colmap model conversion
- [Kapture image cropper script](https://gist.github.com/jo-chemla/258e6e40d3d6c2220b29518ff3c17c40) - undistorted image cropper script to remove black borders with included conversion instructions
- [camorph](https://github.com/Fraunhofer-IIS/camorph) - a toolbox for conversion between camera parameter conventions e.g. Reality Capture to colmap model
- [3DGS Converter](https://github.com/francescofugazzi/3dgsconverter) - a tool for converting 3D Gaussian Splatting .ply files into a format suitable for Cloud Compare and vice-versa.
- [SuperSplat](https://github.com/playcanvas/super-splat) - open source browser-based tool to clean up and reorient .ply files

## Blog Posts

1. [Gaussian Splatting is pretty cool](https://aras-p.info/blog/2023/09/05/Gaussian-Splatting-is-pretty-cool/)
2. [Making Gaussian Splats smaller](https://aras-p.info/blog/2023/09/13/Making-Gaussian-Splats-smaller/)
3. [Making Gaussian Splats more smaller](https://aras-p.info/blog/2023/09/27/Making-Gaussian-Splats-more-smaller/)
4. [Introduction to 3D Gaussian Splatting](https://huggingface.co/blog/gaussian-splatting)
5. [Very good (technical) intro to 3D Gaussian Splatting](https://medium.com/@AriaLeeNotAriel/numbynum-3d-gaussian-splatting-for-real-time-radiance-field-rendering-kerbl-et-al-60c0b25e5544)
6. [Write up on some mathematical details of the 3DGS implementation](https://github.com/kwea123/gaussian_splatting_notes)
7. [Discussion about gs universal format](https://github.com/mkkellogg/GaussianSplats3D/issues/47#issuecomment-1801360116)
8. [Math explanation to understand 3DGS](https://github.com/chiehwangs/3d-gaussian-theory)



## Tutorial Videos

1. [Getting Started with 3DGS for Windows](https://youtu.be/UXtuigy_wYc?si=j1vfORNspcocSH-b)
2. [How to view 3DGS Scenes in Unity](https://youtu.be/5_GaPYBHqOo?si=6u9j1HqXwF_5WSUL)
3. [Two-minute explanation of 3DGS](https://youtu.be/HVv_IQKlafQ?si=w5c9XKHfKIBuXDLW)
4. [Jupyter notebook tutorial](https://www.youtube.com/watch?v=OcvA7fmiZYM&t=2s)
5. [Intro to gaussian splatting (and Unity plugin)](https://www.xuanprada.com/blog/2023/10/22/intro-to-gaussian-splatting)

## Credits

- Thanks to [Leonid Keselman](https://github.com/leonidk) for informing me about the release of the paper "Real-time Photorealistic Dynamic Scene Representation and Rendering with 4D Gaussian Splatting".
- Thanks to [Eric Haines](https://github.com/erich666) for suggesting the jupyter notebook viewer, windows tutorial and for fixing text hyphenations and other issues.
- Thanks to [Henry Pearce](https://github.com/henrypearce4D) for adding more resources and debugging the video links.
