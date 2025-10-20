import * as THREE from "three";

let scene, camera, renderer;
let waveMesh, gridMesh;
const clock = new THREE.Clock();
let mouse = { x: 0, y: 0 };
let scrollY = 0;
const nav = document.getElementById("navbar");

init();
animate();

function init() {
  const container = document.getElementById("bg");

  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 2000);
  camera.position.set(0, 10, 80);

  renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(window.devicePixelRatio);
  renderer.setClearColor(0x020617, 1);
  container.appendChild(renderer.domElement);

  // Foreground wave layer
  const planeGeo = new THREE.PlaneGeometry(200, 200, 120, 120);
  const planeMat = new THREE.MeshBasicMaterial({ color: 0x0b2745, wireframe: true });
  waveMesh = new THREE.Mesh(planeGeo, planeMat);
  waveMesh.rotation.x = -Math.PI / 2.5;
  waveMesh.position.y = -5;
  scene.add(waveMesh);

  // Deep grid "horizon"
  const gridGeo = new THREE.PlaneGeometry(800, 800, 80, 80);
  const gridMat = new THREE.LineBasicMaterial({ color: 0x072033, opacity: 0.3, transparent: true });
  gridMesh = new THREE.LineSegments(new THREE.WireframeGeometry(gridGeo), gridMat);
  gridMesh.rotation.x = -Math.PI / 2.8;
  gridMesh.position.set(0, -100, -100);
  scene.add(gridMesh);

  const ambient = new THREE.AmbientLight(0x203850, 1);
  scene.add(ambient);

  document.addEventListener("mousemove", e => {
    mouse.x = (e.clientX / window.innerWidth - 0.5) * 2;
    mouse.y = (e.clientY / window.innerHeight - 0.5) * 2;
  });

  window.addEventListener("scroll", () => {
    scrollY = window.scrollY;
    // fade navbar on scroll
    const fade = Math.min(scrollY / 300, 1);
    nav.style.opacity = 1 - fade * 0.3;
  });

  window.addEventListener("resize", onResize);
}

function animate() {
  requestAnimationFrame(animate);
  const t = clock.getElapsedTime();

  // Update wave geometry
  const pos = waveMesh.geometry.attributes.position;
  for (let i = 0; i < pos.count; i++) {
    const x = pos.getX(i);
    const y = pos.getY(i);
    const z = Math.sin(x / 6 + t * 1.4) * Math.cos(y / 6 + t * 1.4) * 2;
    pos.setZ(i, z);
  }
  pos.needsUpdate = true;

  // Camera parallax and scroll depth
  camera.position.x += (mouse.x * 10 - camera.position.x) * 0.05;
  camera.position.y += (-mouse.y * 6 - camera.position.y) * 0.05;
  camera.position.z = 80 + scrollY * 0.06;

  // Background grid rotation and depth (apocalyptic effect)
  gridMesh.rotation.z = t * 0.01 + scrollY * 0.0002;
  gridMesh.position.z = -100 + Math.sin(t * 0.3) * 10 - scrollY * 0.15;
  gridMesh.position.y = -100 + Math.sin(t * 0.2) * 5;

  renderer.render(scene, camera);
}

function onResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}