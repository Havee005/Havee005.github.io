#!/usr/bin/env python3
"""Build the project detail pages in projects/<slug>/index.html.

All page content lives in PROJECTS below. To add a photo, GIF or video to a
project, add an entry to its "media" list and run:

    python3 tools/build_projects.py

Media entries:
    {"img": "url or /assets/... path", "caption": "..."}
    {"video": "url or /assets/... path", "caption": "..."}
Any image or video that fails to load is hidden on the page.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GH_ATTACH = "https://github.com/user-attachments/assets/"
VM_ASSETS = "https://github.com/Havee005/VisionMouse/assets/124234544/"

PROJECTS = [
    {
        "slug": "spyder",
        "title": "Spyder",
        "eyebrow": "AUTONOMOUS AGRICULTURAL ROVER",
        "summary": "A six-wheeled autonomous agricultural rover with rocker-bogie suspension, built to navigate rough, unstructured farm terrain.",
        "image": "spyder.jpg",
        "alt": "Spyder six-wheeled rover on pavement",
        "chips": ["Mobile robotics", "Rocker-bogie suspension", "All-terrain navigation", "Agriculture"],
        "links": [("View LinkedIn post", "https://www.linkedin.com/posts/adityapachpute_spyder-rooted-in-tech-rising-in-yield-ugcPost-7328853697474560000-rAJJ", "spyder-post")],
        "stats": [("6", "wheels"), ("Rocker-bogie", "suspension")],
        "sections": [
            ("Overview", [
                "p:Spyder is an autonomous AgRover designed for agricultural fields, where the ground is uneven, soft and unpredictable. The goal was a platform that keeps moving reliably where a typical wheeled robot would get stuck or tip.",
                "p:Its six-wheel rocker-bogie suspension keeps every wheel in contact with the ground over bumps and furrows. The chassis stays stable while the rover collects data in the field.",
            ]),
            ("Highlights", [
                "ul:Six-wheeled chassis with rocker-bogie suspension for all-terrain mobility|Built for robust performance in unstructured, data-driven agricultural environments",
            ]),
        ],
        "media": [],
    },
    {
        "slug": "velo-vision",
        "title": "Velo-Vision",
        "eyebrow": "SENSOR FUSION · AUTONOMOUS VEHICLES",
        "summary": "Late sensor fusion that projects 3D LiDAR point clouds onto 2D camera images to detect and localize vehicles in urban scenes from the KITTI dataset.",
        "image": "velo-vision.jpg",
        "alt": "Clustered LiDAR points projected onto a camera image",
        "chips": ["Python", "OpenCV", "Open3D", "NumPy", "YOLOv4", "RANSAC", "DBSCAN", "KITTI"],
        "links": [("View code", "https://github.com/Havee005/Velo-Vision", "velo-vision")],
        "stats": [("326", "KITTI camera frames processed"), ("2", "sensors fused: LiDAR + camera")],
        "sections": [
            ("Overview", [
                "p:Autonomous vehicles see the world through several sensors at once. A camera gives rich color and texture but no depth; a LiDAR gives precise 3D geometry but no appearance. Velo-Vision brings the two together so the vehicle can perceive both at the same time.",
                "p:It uses late fusion: each sensor is processed on its own to extract high-level results, such as image bounding boxes and LiDAR object clusters. Those results are then combined in one view by projecting the 3D clusters onto the 2D camera frame.",
            ]),
            ("How it works", [
                "steps:Camera detection|A pretrained YOLOv4 model with COCO weights detects and tracks vehicles in KITTI's left RGB camera frames, with no retraining.;"
                "Ground removal|RANSAC segments the dominant ground plane out of the raw LiDAR point cloud, leaving vehicles, poles and other obstacles. It is robust to the noise and sparse outliers of outdoor LiDAR data.;"
                "Clustering|DBSCAN groups the remaining non-ground points into objects by spatial density, so no labelled data is needed.;"
                "Bounding boxes|Axis-aligned bounding boxes are fitted around each cluster, ready to be tracked across frames or matched with camera detections.;"
                "Calibration|The camera intrinsics, rectification matrix and LiDAR-to-camera extrinsics define how points move between the two sensors' coordinate frames.;"
                "Projection|Clustered LiDAR points are transformed into the camera frame and projected onto the image plane, overlaying 3D objects on the 2D detections.",
            ]),
            ("Tools", [
                "ul:Python with OpenCV, Open3D, NumPy and Matplotlib|YOLOv4 object detection (80 COCO classes)|KITTI Vision Benchmark Suite synchronized LiDAR and camera data",
            ]),
        ],
        "media": [
            {"img": GH_ATTACH + "1a252de4-2dcb-4182-bb25-f906cbc81e39", "caption": "Vehicle detection and tracking with YOLOv4 on KITTI frames."},
            {"img": GH_ATTACH + "a815dcbc-0f1c-46c8-bda3-86173cb80a73", "caption": "Raw 3D LiDAR point cloud."},
            {"img": GH_ATTACH + "27d66ed3-1434-486f-b2e0-d5707c10f68f", "caption": "Ground plane removed with RANSAC."},
            {"img": GH_ATTACH + "9ee42237-ec4b-4449-b056-74b2e301ef63", "caption": "Obstacles clustered with DBSCAN."},
            {"img": GH_ATTACH + "7291a75f-a0d3-46da-8de3-30c7d7d94da3", "caption": "Bounding boxes fitted to each cluster."},
            {"img": GH_ATTACH + "b5f89136-34de-4c37-a047-326b86526b8c", "caption": "Clustered LiDAR points projected onto the camera image."},
        ],
    },
    {
        "slug": "visionmouse",
        "title": "VisionMouse",
        "eyebrow": "COMPUTER VISION · ACCESSIBILITY",
        "summary": "Hands-free cursor control: eye movements move the pointer and blinks click, using facial landmarks and a CNN trained on my own eye-gaze dataset.",
        "image": "visionmouse.jpg",
        "image_class": "contain",
        "alt": "Eye with a mouse cursor icon",
        "chips": ["Python", "OpenCV", "MediaPipe", "TensorFlow", "CNN", "scikit-learn", "PyAutoGUI"],
        "links": [("View code", "https://github.com/Havee005/VisionMouse", "visionmouse")],
        "stats": [("9", "gaze classes"), ("~1,000", "images per class"), ("75%", "validation accuracy")],
        "sections": [
            ("Overview", [
                "p:VisionMouse lets you navigate, click and control a computer without touching a mouse or trackpad. It is aimed at accessibility and hands-free computing.",
                "p:A webcam tracks where you are looking and when you blink. A trained model turns gaze into cursor movement, and a deliberate blink becomes a click.",
            ]),
            ("How it works", [
                "steps:Face landmarks|MediaPipe detects the face and its 3D landmarks, then the key eye landmarks are used to locate and crop each eye.;"
                "Dataset|I collected my own dataset of 50×50 eye images across 9 gaze classes, roughly 1,000 images per class, captured frame by frame from video.;"
                "CNN model|A sequential CNN with ReLU activations and a softmax output classifies the gaze direction of each eye, reaching 75% validation accuracy in TensorFlow.;"
                "Blink detection|The eye aspect ratio (EAR) algorithm measures six landmarks per eye to tell an intentional blink from an open eye.;"
                "Cursor control|The predicted eye state drives PyAutoGUI to move the pointer, and a blink triggers a click.",
            ]),
        ],
        "media": [
            {"img": VM_ASSETS + "7be2eebc-e996-4606-83bf-e7d5b547f302", "caption": "Face detection and eye landmarks with MediaPipe."},
            {"img": VM_ASSETS + "ef8c5760-e04d-4e32-9c34-fee48bcb2f3b", "caption": "Part of the eye-gaze training dataset."},
            {"img": VM_ASSETS + "e0e2413e-3d1e-4008-bbd0-042d8f7513ba", "caption": "CNN training accuracy."},
            {"video": VM_ASSETS + "ea36a2a2-cea3-4e99-b541-73cbc4d6f43d", "caption": "Moving the cursor with eye movements."},
            {"video": VM_ASSETS + "9b4a897c-af6c-4f98-835e-7cbfbb69e27d", "caption": "Clicking with a blink."},
        ],
    },
    {
        "slug": "auto-tank",
        "title": "Auto-tank",
        "eyebrow": "INDOOR AUTONOMOUS NAVIGATION · ROS",
        "summary": "An autonomous mobile robot with differential drive that maps and navigates indoor spaces using LiDAR and SLAM on ROS.",
        "image": "auto-tank.jpg",
        "alt": "Auto-tank mobile robot in an indoor hall",
        "chips": ["ROS", "SLAM", "LiDAR", "Differential drive", "Wheel encoders"],
        "links": [],
        "stats": [("Indoor", "autonomous navigation"), ("SLAM", "mapping and localization")],
        "sections": [
            ("Overview", [
                "p:Auto-tank is an autonomous mobile robot built for indoor navigation. It uses a differential drive, steering by changing the speed of its left and right wheels.",
                "p:The robot runs on ROS, with separate nodes for each part of the system, so the hardware, sensing and mapping stay modular and easy to debug.",
            ]),
            ("System", [
                "ul:ROS nodes handle motor commands to the differential drive|Wheel encoder data is read and published for odometry|LiDAR scans are read and fed to SLAM|SLAM builds a map of the space while tracking the robot's position in it",
            ]),
        ],
        "media": [],
    },
    {
        "slug": "flexible-manipulator",
        "title": "Flexible Manipulator",
        "eyebrow": "CONTINUUM ROBOTICS · SOFT ROBOTICS",
        "summary": "A tendon-driven continuum robot arm that bends like an octopus tentacle or elephant trunk, with a soft silicone gripper for fragile objects.",
        "image": "flexible-manipulator.jpg",
        "alt": "Segmented continuum robot arm",
        "chips": ["Arduino Uno", "PCA9685", "I2C", "Servo control", "CAD", "3D printing", "Soft robotics"],
        "links": [("View code", "https://github.com/Havee005/Flexible-Manipulator", "flexible-manipulator")],
        "stats": [("6", "bending segments, 70 mm each"), ("12", "steel tendons"), ("6", "servo motors")],
        "sections": [
            ("Overview", [
                "p:Rigid, jointed arms struggle in tight spaces and with delicate objects. Inspired by octopus tentacles and elephant trunks, this continuum robot bends smoothly along its whole length instead.",
                "p:That flexibility makes this kind of arm suited to minimally invasive surgery and fruit picking. The soft end effector can lift fragile and brittle objects without damaging them.",
            ]),
            ("How it's built", [
                "steps:Continuum arm|Six 3D-printed PLA segments, each 70 mm long. Threaded discs link the segments and let the tendons slide through, so the arm bends without changing length.;"
                "Driving box|Six servo motors pull 12 thin steel tendons through a pulley mechanism, two tendons per segment.;"
                "Control|An Arduino Uno reads a joystick and talks to a PCA9685 PWM servo controller over I2C, which sets each servo's angle.;"
                "Soft gripper|The end effector is cast from two-part liquid silicone rubber in a 3D-printed mold, cured for 6 hours, and actuated by air.",
            ]),
            ("Components", [
                "table:Component|Key specs;"
                "Arduino Uno|ATmega328P, 16 MHz, 5 to 12 V;"
                "PCA9685 servo controller|Up to 16 servos over I2C, 6 V;"
                "MG995 servo motor|Metal gear, 9 kg·cm stall torque, 4.8 to 6 V;"
                "Liquid silicone rubber|1:1 mix, 6-hour cure;"
                "Compressor|12 V, actuates the soft gripper;"
                "Power supply|350 W SMPS",
            ]),
        ],
        "media": [
            {"img": GH_ATTACH + "cf4fed70-9b71-44e7-a259-cb9fb3aa5d8a", "caption": "Continuum arm segments."},
            {"img": GH_ATTACH + "97b45238-7c25-4b84-9f0f-1fc3e6fcdee7", "caption": "How the joystick, Arduino, servo controller and arm connect."},
            {"img": GH_ATTACH + "c60f777f-d809-4c78-bcb2-97c6e3cd6ca9", "caption": "Continuum arm assembly."},
            {"img": GH_ATTACH + "ee5ad736-33b7-4361-a786-0593e2085cc0", "caption": "3D-printed mold for the soft gripper."},
            {"img": GH_ATTACH + "c4fcd13c-7cb3-4ac2-af1c-b0be00811ab6", "caption": "The complete working model."},
            {"video": GH_ATTACH + "a7f8f5ff-005b-416e-a2ee-82453f930020", "caption": "A single segment bending."},
            {"video": GH_ATTACH + "f3ba16c5-ed57-46d7-b09f-91d38812cedd", "caption": "Joystick control of the servos through the PCA9685."},
            {"video": GH_ATTACH + "5b54fa6e-752b-4356-8e0c-c6d8558aac59", "caption": "Soft gripper demo."},
        ],
    },
    {
        "slug": "electric-cycle",
        "title": "Electric Cycle",
        "eyebrow": "ELECTRIC MOBILITY",
        "summary": "An affordable, eco-friendly e-bike converted from a regular bicycle for delivery workers facing rising fuel costs.",
        "image": "electric-cycle.jpg",
        "alt": "Bicycle converted to an electric bike",
        "chips": ["EV conversion", "Sustainable mobility", "Last-mile delivery"],
        "links": [],
        "stats": [("60 km", "range on a full charge"), ("35 km/h", "top speed")],
        "sections": [
            ("Overview", [
                "p:With fuel costs rising, getting around is expensive for delivery workers. We set out to build an affordable, efficient and eco-friendly e-bike for them.",
                "p:Instead of designing a new frame, we modified a regular bicycle. That kept the cost down while delivering a 60 km range on a full charge and speeds up to 35 km/h.",
            ]),
            ("Highlights", [
                "ul:Modified from a standard bicycle to keep costs low|60 km range on a single charge|Top speed of 35 km/h|Tailored to delivery workers",
            ]),
        ],
        "media": [],
    },
    {
        "slug": "wall-cutting-robot",
        "title": "Wall Cutting Robot",
        "eyebrow": "CONSTRUCTION ROBOTICS · WORKER SAFETY",
        "summary": "A smartphone-controlled robot that cuts channels in walls for electrical and plumbing lines, keeping workers away from the dust.",
        "image": "wall-cutting-robot.jpg",
        "alt": "Team presenting the wall cutting robot at an exhibition",
        "chips": ["Wireless control", "Smartphone control", "Construction automation", "Worker safety"],
        "links": [],
        "stats": [("20 m", "wireless control range"), ("Smartphone", "operated")],
        "sections": [
            ("Overview", [
                "p:Cutting channels into walls for wiring and pipes fills the air with dust that workers end up breathing in, which is a real health risk on construction sites.",
                "p:This robot automates the job. A worker controls it from a smartphone up to 20 meters away, so the robot carves the channel while the worker stays clear of the dust.",
            ]),
            ("Highlights", [
                "ul:Smartphone control within a 20-meter range|Cuts channels for electrical and plumbing lines|Reduces dust exposure and related health risks for workers",
            ]),
        ],
        "media": [
            {"img": "/assets/img/wall-cutting-robot.jpg", "caption": "Presenting the wall cutting robot at an exhibition."},
        ],
    },
]

ICONS = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="i-phone" viewBox="0 0 24 24"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></symbol>
</svg>'''


def render_block(block):
    kind, _, body = block.partition(":")
    if kind == "p":
        return f"<p>{escape(body)}</p>"
    if kind == "ul":
        items = "".join(f"<li>{escape(x)}</li>" for x in body.split("|"))
        return f"<ul>{items}</ul>"
    if kind == "steps":
        out = []
        for step in body.split(";"):
            title, text = step.split("|", 1)
            out.append(f"<li><h3>{escape(title)}</h3><p>{escape(text)}</p></li>")
        return f'<ol class="steps">{"".join(out)}</ol>'
    if kind == "table":
        rows = [r.split("|") for r in body.split(";")]
        head = "".join(f'<th scope="col">{escape(c)}</th>' for c in rows[0])
        trs = "".join("<tr>" + "".join(f"<td>{escape(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
        return f'<div class="table-wrap"><table><thead><tr>{head}</tr></thead><tbody>{trs}</tbody></table></div>'
    raise ValueError(kind)


def render_media(m):
    cap = escape(m["caption"])
    if "video" in m:
        el = f'<video src="{escape(m["video"])}" controls muted playsinline preload="metadata" aria-label="{cap}"></video>'
    else:
        el = f'<img src="{escape(m["img"])}" alt="{cap}">'
    return f"<figure>{el}<figcaption>{cap}</figcaption></figure>"


def page(i, p):
    prev_p = PROJECTS[i - 1] if i > 0 else None
    next_p = PROJECTS[i + 1] if i < len(PROJECTS) - 1 else None
    chips = "".join(f"<li>{escape(c)}</li>" for c in p["chips"])
    links = "".join(
        f'<a class="btn" data-goatcounter-click="project-{gc}" href="{escape(url)}" target="_blank" rel="noopener">{escape(label)} <span aria-hidden="true">&#8599;</span></a>'
        for label, url, gc in p["links"]
    )
    links += '<a class="btn ghost" href="/#message">Ask me about it</a>'
    stats = "".join(f"<li><b>{escape(n)}</b><span>{escape(l)}</span></li>" for n, l in p["stats"])
    sections = "".join(
        f'<section><div class="wrap"><h2>{escape(h)}</h2><div class="prose">{"".join(render_block(b) for b in blocks)}</div></div></section>'
        for h, blocks in p["sections"]
    )
    if p["media"]:
        media = f'<div class="gallery">{"".join(render_media(m) for m in p["media"])}</div>'
    else:
        media = '<p class="coming-soon">Photos and videos of this build are coming soon.</p>'
    img_class = f' class="{p["image_class"]}"' if p.get("image_class") else ""
    pager = ""
    if prev_p:
        pager += f'<a class="prev" href="/projects/{prev_p["slug"]}/"><small>&#8592; PREVIOUS</small><strong>{escape(prev_p["title"])}</strong></a>'
    if next_p:
        pager += f'<a class="next" href="/projects/{next_p["slug"]}/"><small>NEXT &#8594;</small><strong>{escape(next_p["title"])}</strong></a>'
    title = escape(p["title"])
    summary = escape(p["summary"])
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title} · Haveenash Umamaheswaran</title>
<meta name="description" content="{summary}">
<meta property="og:title" content="{title} · Haveenash Umamaheswaran">
<meta property="og:description" content="{summary}">
<meta property="og:image" content="https://havee005.github.io/assets/img/{p["image"]}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&display=swap">
<link rel="stylesheet" href="/assets/css/project.css">
</head>
<body>
<!-- Generated by tools/build_projects.py. Edit the data there, not this file. -->
<header class="topbar"><div class="wrap">
  <a href="/">&#8592; HAVEENASH UMAMAHESWARAN</a>
  <a href="/#projects">ALL PROJECTS</a>
</div></header>

<div class="hero"><div class="wrap">
  <div>
    <p class="eyebrow">{escape(p["eyebrow"])}</p>
    <h1>{title}</h1>
    <p class="summary">{summary}</p>
    <ul class="chips" aria-label="Tools and topics">{chips}</ul>
    <div class="actions">{links}</div>
  </div>
  <div class="rings"><img src="/assets/img/{p["image"]}"{img_class} alt="{escape(p["alt"])}"></div>
</div></div>

<div class="stats"><div class="wrap"><ul aria-label="Key numbers">{stats}</ul></div></div>

<main>
{sections}
<section id="media"><div class="wrap"><h2>Photos &amp; Videos</h2>{media}</div></section>
</main>

<nav class="pager" aria-label="More projects"><div class="wrap">{pager}</div></nav>

<footer><div class="wrap">
  <ul>
    <li><a data-goatcounter-click="link-email" href="mailto:haveenashsrm@gmail.com">haveenashsrm@gmail.com</a></li>
    <li><a data-goatcounter-click="link-linkedin" href="https://www.linkedin.com/in/haveenash-umamaheswaran/" target="_blank" rel="noopener">LinkedIn</a></li>
    <li><a data-goatcounter-click="link-github" href="https://github.com/Havee005" target="_blank" rel="noopener">GitHub</a></li>
  </ul>
  <small>© <span id="yr">2026</span> Haveenash Umamaheswaran</small>
</div></footer>

<script>
  // Hide any photo or video that fails to load, so visitors never see a broken box.
  // If nothing in the gallery loads, show the "coming soon" note instead.
  (function () {{
    var gallery = document.querySelector('.gallery');
    if (!gallery) return;
    function hide(el) {{
      el.closest('figure').hidden = true;
      if (!gallery.querySelector('figure:not([hidden])')) {{
        var note = document.createElement('p');
        note.className = 'coming-soon';
        note.textContent = 'Photos and videos of this build are coming soon.';
        gallery.replaceWith(note);
      }}
    }}
    gallery.querySelectorAll('img').forEach(function (el) {{
      if (el.complete && el.naturalWidth === 0) hide(el);
      else el.addEventListener('error', function () {{ hide(el); }});
    }});
    gallery.querySelectorAll('video').forEach(function (el) {{
      if (el.error || el.networkState === 3) hide(el);
      else el.addEventListener('error', function () {{ hide(el); }});
    }});
  }})();
  document.getElementById('yr').textContent = new Date().getFullYear();
</script>
<!-- Visitor stats: https://havee005.goatcounter.com -->
<script data-goatcounter="https://havee005.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
</body>
</html>
'''


def main():
    for i, p in enumerate(PROJECTS):
        out = ROOT / "projects" / p["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(i, p), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
