---
title: Zometool 入门
date: 2026-07-08
subtitle: Zometool 球和棍的几何
share-description: Zometool 球和棍的基础几何中文简介
image: Zometool-intro-zh.png
layout: page
---

<style>
  section.zometool-intro {
    height: 90vh;
    width: 100%;
    margin: auto;
    overflow: hidden;
    resize: both;
    gap: 1em;
    display: grid;
    grid-template-rows: min-content min-content 1fr;
    background: rgba(0, 0, 0, 0.4);
    padding: 1em;
  }

  .zometool-intro .flex {
    display: flex;
    align-items: center;
  }

  .zometool-intro .vzome-viewer-index-button {
    min-width: 90px;
    font-size: large;
    border-radius: 6px;
    border-style: solid;
    border-color: black;
    background-color: aliceblue;
  }

  .zometool-intro vzome-viewer {
    width: 100%;
    height: 100%;
  }

  #title {
    padding-inline-start: 2rem;
    margin-block: 0.5rem;
  }

  #description {
    height: 200px;
  }
</style>

<script type="module">
  import "https://www.vzome.com/modules/vzome-viewer.js";

  let scenes;
  const translatedScenes = [
    {
      title: "球",
      content: "Zometool 的球有 62 个孔，排列成二十面体对称。三十个长方形孔用于蓝棍，二十个三角形孔用于黄棍，十二个五边形孔用于红棍。"
    },
    {
      title: "蓝色方向",
      content: "蓝色直线定义了十五个镜面。这些镜面组成一个球面万花筒，生成二十面体反射群。每个镜面都垂直于一条蓝色直线，并对应球表面上一对相对的长方形孔。"
    },
    {
      title: "红色方向",
      content: "红色直线出现在五个镜面的交线上，因此对应五重旋转对称。这就是红棍使用五边形截面的原因。"
    },
    {
      title: "黄色方向",
      content: "黄色直线出现在三个镜面的交线上，因此对应三重旋转对称。这就是黄棍使用三角形截面的原因。"
    },
    {
      title: "蓝色正交框架",
      content: "每一条蓝色直线都可以和另外两条蓝色直线组成一个正交框架。这样的框架一共有五组。这意味着我们可以搭出五个立方体的复合体，尽管整个 Zometool 系统本身并没有真正的立方对称。"
    },
    {
      title: "十二面体",
      content: "Zometool 天然支持用蓝色方向搭建五边形和十二面体。十二面体的中心决定了黄棍相对于蓝棍的长度。在一个连通的 Zome 结构中，所有球的朝向都是一致的。合法拼搭不需要弯曲或扭转。"
    },
    {
      title: "对偶化",
      content: "我们可以把十二面体的每一条边替换为大一号并与它正交的蓝棍。"
    },
    {
      title: "对偶多面体",
      content: "如果在所有边上都这样替换，就得到二十面体，也就是十二面体的对偶。"
    },
    {
      title: "二十面体",
      content: "二十面体的中心决定了红棍相对于蓝棍的长度。"
    },
    {
      title: "蓝棍长度",
      content: "Zometool 的棍有三种常用长度，相邻长度之间按黄金比例缩放。"
    },
    {
      title: "较老套装中的蓝棍",
      content: "较老的 Zometool 套装整体大一个尺度：包含 B3 棍，但没有 B0 棍。"
    },
    {
      title: "红棍长度",
      content: "红棍也有三种常用长度，同样按黄金比例缩放。"
    },
    {
      title: "较老套装中的红棍",
      content: "较老的 Zometool 套装包含 R3 棍，但没有 R0 棍。"
    },
    {
      title: "黄棍长度",
      content: "黄棍也有三种常用长度，同样按黄金比例缩放。"
    },
    {
      title: "较老套装中的黄棍",
      content: "较老的 Zometool 套装包含 Y3 棍，但没有 Y0 棍。"
    }
  ];

  const welcomeViewer = document.getElementById("welcome");
  const titleText = document.getElementById("title");
  const descriptionText = document.getElementById("description");

  welcomeViewer.addEventListener("vzome-scenes", ({ detail }) => {
    scenes = [...detail];
  });
  welcomeViewer.addEventListener("vzome-design-rendered", ({ detail: scene }) => {
    const { index } = scene;
    const translatedScene = translatedScenes[index] || scenes[index];
    titleText.textContent = translatedScene.title;
    descriptionText.value = translatedScene.content;
  });
</script>

<section class="zometool-intro">
  <div class="flex">
    <vzome-viewer-previous label="上一步" load-camera="true" viewer="welcome" class="hidden">
    </vzome-viewer-previous>

    <vzome-viewer-next label="下一步" load-camera="true" viewer="welcome" class="hidden">
    </vzome-viewer-next>

    <h1 id="title"></h1>
  </div>

  <textarea id="description" readonly></textarea>

  <vzome-viewer id="welcome" indexed="true" src="Zometool-intro-zh.vZome">
    <img style="width: 100%" src="Zometool-intro-zh.png">
  </vzome-viewer>
</section>

<p style="margin-top: 1em;">
  这是 Scott Vorthmann 的 <a href="https://www.vzome.com/docs/zometool-intro.html">Introduction to Zometool</a>
  的中文翻译版本。原始 vZome 模型和英文说明由 Scott Vorthmann 创建；中文翻译由马楠整理。
</p>
