---
title: Approximate Zome Spheres
date: 2026-07-26
share-description: Hollow Zometool shells whose balls all lie on one sphere.
image: ball_960_a.png
layout: vzome
---

Each model is a hollow Zometool shell: every ball sits on one thin spherical
shell centred on the origin, and every edge of the convex hull is a **single**
standard strut (RGBY, scales 0-3, no concatenation). There is no ball at the
centre, and face diagonals are not struts.

Drag to rotate any model. The still image is replaced by the interactive
version once it finishes loading.

<script type='module' src='https://www.vzome.com/modules/vzome-viewer.js'></script>

<style>
  .approx-model {
    box-sizing: border-box;
    border: 1px solid #ddd;
    border-radius: 0.5rem;
    background: #fff;
    margin: 2rem auto;
    max-width: min(100%, 72dvh);
    padding: 0.25rem;
    width: 100%;
  }
  .approx-model vzome-viewer {
    display: block;
    width: 100%;
    aspect-ratio: 1 / 1;
    height: auto;
  }
  .approx-model vzome-viewer img {
    width: 100%;
    height: auto;
  }
  .approx-model figcaption {
    color: #24292f;
    margin: 0.75rem 0 0.5rem;
    text-align: center;
  }
  .approx-model figcaption .model-title {
    display: block;
    font-weight: 600;
  }
  .approx-model figcaption .model-note {
    color: #57606a;
    display: block;
    margin-top: 0.2rem;
  }
</style>

<figure class="approx-model">
 <vzome-viewer src="ball_240_a.vZome" progress="true" >
  <img src="ball_240_a.png" alt="240 balls (variant a) 420 struts" >
 </vzome-viewer>
 <figcaption>
  <span class="model-title">240 balls (variant a) 420 struts</span>
  <span class="model-note">Every ball lies on one sphere.</span>
 </figcaption>
</figure>

<figure class="approx-model">
 <vzome-viewer src="ball_240_b.vZome" progress="true" >
  <img src="ball_240_b.png" alt="240 balls (variant b) 420 struts" >
 </vzome-viewer>
 <figcaption>
  <span class="model-title">240 balls (variant b) 420 struts</span>
  <span class="model-note">Every ball lies on one sphere.</span>
 </figcaption>
</figure>

<figure class="approx-model">
 <vzome-viewer src="ball_240_c.vZome" progress="true" >
  <img src="ball_240_c.png" alt="240 balls (variant c) 450 struts" >
 </vzome-viewer>
 <figcaption>
  <span class="model-title">240 balls (variant c) 450 struts</span>
  <span class="model-note">Every ball lies on one sphere.</span>
 </figcaption>
</figure>

<figure class="approx-model">
 <vzome-viewer src="ball_360.vZome" progress="true" >
  <img src="ball_360.png" alt="360 balls 660 struts" >
 </vzome-viewer>
 <figcaption>
  <span class="model-title">360 balls 660 struts</span>
  <span class="model-note">Ratios between radii &asymp; 99.96%</span>
 </figcaption>
</figure>

<figure class="approx-model">
 <vzome-viewer src="ball_960_b.vZome" progress="true" >
  <img src="ball_960_b.png" alt="960 balls (variant b) 1500 struts" >
 </vzome-viewer>
 <figcaption>
  <span class="model-title">960 balls (variant b) 1500 struts</span>
  <span class="model-note">Ratios between radii &asymp; 99.48%</span>
 </figcaption>
</figure>

<figure class="approx-model">
 <vzome-viewer src="ball_960_a.vZome" progress="true" >
  <img src="ball_960_a.png" alt="960 balls (variant a) 1500 struts" >
 </vzome-viewer>
 <figcaption>
  <span class="model-title">960 balls (variant a) 1500 struts</span>
  <span class="model-note">Ratios between radii &asymp; 99.48%</span>
 </figcaption>
</figure>
