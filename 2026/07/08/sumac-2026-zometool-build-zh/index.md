---
title: 2026 Zometool 搭建活动
date: 2026-07-08
share-description: 搭建大型 Zometool 穹顶的中文说明
image: SUMaC-2026-final-scenes.png
layout: vzome
---

{% comment %}
中文版本基于 Scott Vorthmann 的 SUMaC 2026 Zome Build 页面：
https://vorth.github.io/vzome-sharing/2026/07/02/SUMaC-2026-Zometool-Build-13-52-17-489Z.html
{% endcomment %}

<script type="module" src="https://www.vzome.com/modules/zometool.js"></script>
<script>
  (() => {
    const localizeText = (root) => {
      const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
      for (let node = walker.nextNode(); node; node = walker.nextNode()) {
        if (node.nodeValue.includes("Show Build Steps")) {
          node.nodeValue = node.nodeValue.replaceAll("Show Build Steps", "显示搭建步骤");
        }
      }
    };

    const localizeViewer = (viewer) => {
      const root = viewer.shadowRoot;
      if (!root) {
        return;
      }
      localizeText(root);
      if (!viewer.zometoolZhObserver) {
        viewer.zometoolZhObserver = new MutationObserver(() => localizeText(root));
        viewer.zometoolZhObserver.observe(root, {
          childList: true,
          subtree: true,
          characterData: true
        });
      }
    };

    const localizeZometoolInstructions = () => {
      document.querySelectorAll("zometool-instructions").forEach(localizeViewer);
    };

    document.addEventListener("DOMContentLoaded", () => {
      customElements.whenDefined("zometool-instructions").then(localizeZometoolInstructions);
      new MutationObserver(localizeZometoolInstructions)
        .observe(document.body, { childList: true, subtree: true });

      let retries = 0;
      const retry = setInterval(() => {
        localizeZometoolInstructions();
        retries += 1;
        if (retries >= 60) {
          clearInterval(retry);
        }
      }, 500);
    });
  })();
</script>
<style>
  .parts-inventory {
    margin: 1em 2% 2em;
  }

  .parts-inventory table {
    width: auto;
  }

  .parts-inventory th,
  .parts-inventory td {
    padding: 0.25em 0.75em;
  }

  .parts-inventory td.part-blue {
    background-color: #dbeafe;
  }

  .parts-inventory td.part-red {
    background-color: #fee2e2;
  }

  .parts-inventory td.part-yellow {
    background-color: #fef9c3;
  }

  .parts-inventory td.part-green {
    background-color: #dcfce7;
  }
</style>

<p>
  今天我们要搭建一个大型 Zometool 模型：一个截半二十面体形状的穹顶。模型直径接近两米。
</p>

<p>
  本中文说明基于 Scott Vorthmann 为 SUMaC 2026 活动创建的英文搭建说明和 vZome 模型。
  原始英文页面在
  <a href="https://vorth.github.io/vzome-sharing/2026/07/02/SUMaC-2026-Zometool-Build-13-52-17-489Z.html">这里</a>；
  中文翻译和活动说明由马楠整理。
</p>

<p>
  如果你第一次接触 Zometool，可以先看
  <a href="../zometool-intro-zh/">Zometool 入门中文说明</a>。
</p>

<p>
  下面先看整个结构和各个模块的概览。你可以打开“显示搭建步骤”开关；
  这些步骤主要是用来说明结构和分工，不一定是严格的逐步搭建顺序。
</p>

<figure style="width: 93%; margin: 2%">
  <zometool-instructions style="width: 100%; height: 80dvh" module="overview"
        src="SUMaC-2026-final-scenes.vZome">
    <img style="width: 100%" src="SUMaC-2026-final-scenes.png">
  </zometool-instructions>

  <figcaption style="text-align: center; font-style: italic;">
    我们要搭建的整体模型
  </figcaption>
</figure>

<p>搭建时建议分成六个小组：</p>

<ul>
  <li>一个小组负责搭建 25 个连接件（junctions）和 5 个底脚（feet）。</li>
  <li>五个小组分别搭建 3 个面模块（face modules），总共 15 个。</li>
</ul>

<p>
  <img alt="搭建小组分工概览" src="teams-overview.png">
</p>

<p>
  各个模块准备好之后，我们会从地面开始，逐层向上组装整个穹顶。
</p>

<div class="parts-inventory">
  <p><strong>总零件清单（25 个连接件、5 个底脚、15 个面模块）</strong></p>
  <table>
    <tbody>
      <tr><td class="part-blue">B1</td><td class="part-blue">395</td><td class="part-blue">B2</td><td class="part-blue">410</td><td class="part-blue">B3</td><td class="part-blue">360</td></tr>
      <tr><td class="part-red">R1</td><td class="part-red">50</td><td class="part-red">R2</td><td class="part-red">280</td><td class="part-red">R3</td><td class="part-red">100</td></tr>
      <tr><td class="part-yellow">Y1</td><td class="part-yellow">60</td><td class="part-yellow">Y2</td><td class="part-yellow">350</td><td class="part-yellow">Y3</td><td class="part-yellow">230</td></tr>
      <tr><td class="part-green">G1</td><td class="part-green">190</td><td></td><td></td><td>球</td><td>765</td></tr>
    </tbody>
  </table>
</div>

<h2>连接件和底脚（一个小组）</h2>

<p>这个小组需要同时完成 25 个连接件和 5 个底脚。</p>

<p>我们需要 <strong><em>25</em></strong> 个这样的连接件：</p>

<figure style="width: 93%; margin: 2%">
  <zometool-instructions style="width: 100%; height: 80dvh" module="junction"
        src="trussed-icosido-steps-lifelike.vZome">
    <img style="width: 100%" src="trussed-icosido-steps-lifelike.png">
  </zometool-instructions>

  <figcaption style="text-align: center; font-style: italic;">
    连接件（共 25 个）
  </figcaption>
</figure>

<div class="parts-inventory">
  <p><strong>起步定标：</strong>先用 1 根 B2 和 2 根 R2 搭起始三角形；之后按 3D 图继续。</p>
  <p><strong>单个连接件零件清单</strong></p>
  <table>
    <tbody>
      <tr><td class="part-blue">B1</td><td class="part-blue"></td><td class="part-blue">B2</td><td class="part-blue">1</td><td class="part-blue">B3</td><td class="part-blue"></td></tr>
      <tr><td class="part-red">R1</td><td class="part-red"></td><td class="part-red">R2</td><td class="part-red">2</td><td class="part-red">R3</td><td class="part-red"></td></tr>
      <tr><td class="part-yellow">Y1</td><td class="part-yellow">2</td><td class="part-yellow">Y2</td><td class="part-yellow">2</td><td class="part-yellow">Y3</td><td class="part-yellow">2</td></tr>
      <tr><td class="part-green">G1</td><td class="part-green"></td><td></td><td></td><td>球</td><td>6</td></tr>
    </tbody>
  </table>
</div>

<p>
  我们还需要 <strong><em>5</em></strong> 个底脚，用来放在地面上支撑整个结构。
  注意：底脚模型里有些棍的一端没有球，因为这些球会由连接件提供。
  如果方便，也可以先给每个底脚装上一个连接件。
</p>

<figure style="width: 93%; margin: 2%">
  <zometool-instructions style="width: 100%; height: 80dvh" module="foot"
        src="trussed-icosido-steps-lifelike.vZome">
    <img style="width: 100%" src="trussed-icosido-steps-lifelike.png">
  </zometool-instructions>

  <figcaption style="text-align: center; font-style: italic;">
    底脚模块（共 5 个）
  </figcaption>
</figure>

<div class="parts-inventory">
  <p><strong>起步定标：</strong>先用 1 根 B1 和 2 根 B2 搭起始三角形；之后按 3D 图继续。</p>
  <p><strong>单个底脚零件清单</strong></p>
  <table>
    <tbody>
      <tr><td class="part-blue">B1</td><td class="part-blue">7</td><td class="part-blue">B2</td><td class="part-blue">14</td><td class="part-blue">B3</td><td class="part-blue"></td></tr>
      <tr><td class="part-red">R1</td><td class="part-red">1</td><td class="part-red">R2</td><td class="part-red">1</td><td class="part-red">R3</td><td class="part-red">2</td></tr>
      <tr><td class="part-yellow">Y1</td><td class="part-yellow">2</td><td class="part-yellow">Y2</td><td class="part-yellow">6</td><td class="part-yellow">Y3</td><td class="part-yellow"></td></tr>
      <tr><td class="part-green">G1</td><td class="part-green">2</td><td></td><td></td><td>球</td><td>12</td></tr>
    </tbody>
  </table>
</div>

<h2>面模块（五个小组）</h2>

<p>
  每个面模块小组需要搭建 <strong><em>3</em></strong> 个这样的结构。
  五个小组合起来，总共需要 15 个面模块。
  注意：这里也有些棍的一端没有球；最后组装时，这些球会由连接件提供。
</p>

<figure style="width: 93%; margin: 2%">
  <zometool-instructions style="width: 100%; height: 80dvh" module="face unit"
        src="trussed-icosido-steps-lifelike.vZome">
    <img style="width: 100%" src="trussed-icosido-steps-lifelike.png">
  </zometool-instructions>

  <figcaption style="text-align: center; font-style: italic;">
    面模块（共 15 个）
  </figcaption>
</figure>

<div class="parts-inventory">
  <p><strong>起步定标：</strong>先用 12 根 B3 搭起始六边形；之后按 3D 图继续。</p>
  <p><strong>单个面模块零件清单</strong></p>
  <table>
    <tbody>
      <tr><td class="part-blue">B1</td><td class="part-blue">24</td><td class="part-blue">B2</td><td class="part-blue">21</td><td class="part-blue">B3</td><td class="part-blue">24</td></tr>
      <tr><td class="part-red">R1</td><td class="part-red">3</td><td class="part-red">R2</td><td class="part-red">15</td><td class="part-red">R3</td><td class="part-red">6</td></tr>
      <tr><td class="part-yellow">Y1</td><td class="part-yellow"></td><td class="part-yellow">Y2</td><td class="part-yellow">18</td><td class="part-yellow">Y3</td><td class="part-yellow">12</td></tr>
      <tr><td class="part-green">G1</td><td class="part-green">12</td><td></td><td></td><td>球</td><td>37</td></tr>
    </tbody>
  </table>
</div>

<h2>最终组装</h2>

<p>
  最终组装时，我们从地面开始，逐层往上搭建。
</p>

<figure style="width: 93%; margin: 2%">
  <zometool-instructions style="width: 100%; height: 80dvh" module="assembly"
        src="SUMaC-2026-final-scenes.vZome">
    <img style="width: 100%" src="SUMaC-2026-final-scenes.png">
  </zometool-instructions>

  <figcaption style="text-align: center; font-style: italic;">
    最终组装
  </figcaption>
</figure>

<h2>资源</h2>

<ul>
  <li><a href="../zometool-intro-zh/">Zometool 入门中文说明</a></li>
  <li><a href="https://www.zometool.com.cn">Zometool 中国</a></li>
  <li><a href="https://www.zometool.com">Zometool 美国、欧洲、日本和韩国</a></li>
  <li><a href="https://www.vzome.com/app">vZome 软件（免费）</a>：用于设计结构并生成这个网页</li>
  <li><a href="https://vorth.github.io/vzome-sharing/2026/07/02/SUMaC-2026-Zometool-Build-13-52-17-489Z.html">Scott Vorthmann 的英文原版说明</a></li>
</ul>
