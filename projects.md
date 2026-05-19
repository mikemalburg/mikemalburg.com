---
layout: default
title: Projects
---

<div class="projects">
  <h1>Projects</h1>
  <div class="projects-grid">
    {% for project in site.projects %}
    <div class="project-card">
      <h2>{{ project.title }}</h2>
      <p>{{ project.description }}</p>
      <a href="{{ project.link }}" class="btn">View Project</a>
    </div>
    {% endfor %}
  </div>
</div>
