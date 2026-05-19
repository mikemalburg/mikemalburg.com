---
layout: default
title: Home
---

{% assign page = site.pages | where: 'path', 'index.md' | first %}

<div class="home">
  <div class="profile">
    <img src="{{ site.baseurl }}/assets/mike-profile.jpg" alt="Mike Malburg" class="profile-img">
    <h1>Mike Malburg</h1>
    <p>Software Engineer &amp; Consultant</p>
  </div>

  <div class="intro">
    <p>Welcome to my personal website. I'm a software engineer with expertise in building scalable applications and embedded systems.</p>
  </div>

  <div class="interests">
    <h2>Interests</h2>
    <ul>
      <li>Golf</li>
      <li>Disc Golf</li>
      <li>Coding</li>
      <li>Hobby Electronics</li>
      <li>Walking</li>
      <li>Popcorn</li>
    </ul>
  </div>

  <div class="links">
    <a href="{{ site.baseurl }}/resume" class="btn">View Resume</a>
    <a href="{{ site.baseurl }}/contact" class="btn btn-outline">Contact Me</a>
    <a href="https://github.com/mikemalburg" class="btn btn-outline">GitHub</a>
    <a href="https://www.linkedin.com/in/mikemalburg" class="btn btn-outline">LinkedIn</a>
  </div>

  <div class="contact">
    <p>Email: <a href="mailto:mikemalburg@gmail.com">mikemalburg@gmail.com</a></p>
    <p>Location: Holt, MI</p>
  </div>
</div>
