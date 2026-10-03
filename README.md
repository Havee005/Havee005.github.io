# Havee005.github.io

Personal robotics portfolio of **Haveenash Umamaheswaran**: Robotic Engineer, Sensor Fusion & Controls, ROS Developer.

Live site: https://havee005.github.io

## What's here

- `index.html`: the whole site (home panels, about, projects carousel, timeline, contact form). Styles and scripts are inline.
- `projects/<name>/index.html`: one detail page per project, generated from `tools/build_projects.py`.
- `assets/css/project.css`: styles for the project pages.
- `assets/img/`: project photos and organization logos.
- `.nojekyll`: tells GitHub Pages to serve the files as they are.

## Editing

- **Text:** edit `index.html` directly. Each section is marked with a comment (`About`, `Projects`, `Timeline`, …).
- **Add a project:** copy one `<article class="project">…</article>` block in the Projects section and change the image, title, text and link.
- **Colors:** change the `--teal-*` values at the top of the `<style>` block. Every text/background pair currently meets WCAG AA contrast.
- **Project pages:** edit the `PROJECTS` list in `tools/build_projects.py`, then run `python3 tools/build_projects.py`. To add a photo, GIF or video, add `{"img": "…", "caption": "…"}` or `{"video": "…", "caption": "…"}` to that project's `media` list. Files can go in `assets/img/projects/` and be referenced as `/assets/img/projects/<file>`.
- **Contact form:** messages go through Formspree (`action="https://formspree.io/f/…"` on the form).

Changes pushed to `main` go live within a minute or two.
