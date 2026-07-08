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

  const welcomeViewer = document.getElementById("welcome");
  const titleText = document.getElementById("title");
  const descriptionText = document.getElementById("description");

  welcomeViewer.addEventListener("vzome-scenes", ({ detail }) => {
    scenes = [...detail];
  });
  welcomeViewer.addEventListener("vzome-design-rendered", ({ detail: scene }) => {
    const { index } = scene;
    titleText.textContent = scenes[index].title;
    descriptionText.value = scenes[index].content;
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
