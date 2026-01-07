document.addEventListener('DOMContentLoaded', function () {

  /* =========================
     AOS INITIALIZATION
  ========================== */
  AOS.init({
    duration: 1000,
    once: true,
    easing: 'ease-in-cubic'
  });

  /* =========================
     COUNT-UP ANIMATION
  ========================== */
  const counters = document.querySelectorAll('.counter');
  const ratioCounters = document.querySelectorAll('.counter-ratio');
  const speed = 50;

  const animateCounter = (counter) => {
    const target = +counter.getAttribute('data-target');
    let count = 0;

    const update = () => {
      const increment = target / speed;
      if (count < target) {
        count += increment;
        counter.innerText = Math.ceil(count);
        setTimeout(update, 30);
      } else {
        counter.innerText = target;
      }
    };

    update();
  };

  const observer = new IntersectionObserver(
    entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.6 }
  );

  counters.forEach(counter => observer.observe(counter));
  ratioCounters.forEach(counter => observer.observe(counter));

  /* =========================
     AUTO SCROLL ROWS
  ========================== */
  const scrollLeftRow = document.getElementById('scroll-left');
  const scrollRightRow = document.getElementById('scroll-right');
  let leftPos = 0;
  let rightPos = 0;
  const speedScroll = 1;

  function animateScroll() {
    if (scrollLeftRow) {
      leftPos += speedScroll;
      if (leftPos >= scrollLeftRow.scrollWidth - scrollLeftRow.clientWidth) leftPos = 0;
      scrollLeftRow.scrollLeft = leftPos;
    }

    if (scrollRightRow) {
      rightPos -= speedScroll;
      if (rightPos <= 0) rightPos = scrollRightRow.scrollWidth - scrollRightRow.clientWidth;
      scrollRightRow.scrollLeft = rightPos;
    }

    requestAnimationFrame(animateScroll);
  }

  if (scrollLeftRow || scrollRightRow) animateScroll();

  /* =========================
     GALLERY MODAL PREVIEW
  ========================== */
  const modal = document.getElementById("galleryModal");
  if (modal) {
    modal.addEventListener("show.bs.modal", function (event) {
      const trigger = event.relatedTarget;
      if (!trigger) return;

      const imageSrc = trigger.dataset.image;
      const title = trigger.dataset.title;
      const category = trigger.dataset.category;
      const date = trigger.dataset.date;

      const img = modal.querySelector(".gallery-modal-image");
      const titleEl = modal.querySelector(".modal-title");
      const metaEl = modal.querySelector(".modal-meta");

      img.src = imageSrc || "";
      titleEl.textContent = title || "";
      metaEl.textContent = (category && date) ? `${category} • ${date}` : "";
    });

    modal.addEventListener("hidden.bs.modal", function () {
      modal.querySelector(".gallery-modal-image").src = "";
    });
  }

  /* =========================
     ADMISSION FORM MULTI-STEP
  ========================== */
  let currentStep = 0;
  const steps = [
    document.querySelector('.section-student'),
    document.querySelector('.section-parent'),
    document.querySelector('.section-medical')
  ];

  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');
  const submitBtn = document.getElementById('submitBtn');
  const stepIndicator = document.getElementById('currentStep');
  const progressBar = document.getElementById('formProgress');

  function showStep(n) {
    steps.forEach((step, index) => {
      if (step) step.style.display = index === n ? 'block' : 'none';
    });

    prevBtn.style.display = n === 0 ? 'none' : 'inline-block';
    nextBtn.style.display = n === steps.length - 1 ? 'none' : 'inline-block';
    submitBtn.style.display = n === steps.length - 1 ? 'inline-block' : 'none';

    stepIndicator.innerText = n + 1;
    progressBar.style.width = ((n + 1) / steps.length) * 100 + '%';
  }

  

  function nextPrev(n) {
    if (n === 1 && !validateStep()) return false;
    currentStep += n;
    showStep(currentStep);
  }

  function validateStep() {
    let valid = true;
    const inputs = steps[currentStep].querySelectorAll('input, select, textarea');
    inputs.forEach(input => {
      if (input.hasAttribute('required') && !input.value) {
        input.classList.add('is-invalid');
        valid = false;
      } else {
        input.classList.remove('is-invalid');
      }
    });
    return valid;
  }

  // attach click events
  if (prevBtn) prevBtn.addEventListener('click', () => nextPrev(-1));
  if (nextBtn) nextBtn.addEventListener('click', () => nextPrev(1));

  // initial display
  showStep(currentStep);


  const lifeConditionSelect = document.querySelector(
    'select[name="life_threatening_condition"]'
  );
  const conditionWrapper = document.getElementById('conditionDetailsWrapper');
  const conditionInput = document.querySelector(
    'textarea[name="condition_details"]'
  );

  const medicationSelect = document.querySelector(
    'select[name="medication_needed"]'
  );
  const medicationWrapper = document.getElementById('medicationDetailsWrapper');
  const medicationInput = document.querySelector(
    'textarea[name="medication_details"]'
  );

  function toggleConditionDetails() {
    if (!lifeConditionSelect || !conditionWrapper) return;

    if (lifeConditionSelect.value === 'Yes') {
      conditionWrapper.style.display = 'block';
    } else {
      conditionWrapper.style.display = 'none';
      if (conditionInput) conditionInput.value = '';
    }
  }

  function toggleMedicationDetails() {
    if (!medicationSelect || !medicationWrapper) return;

    if (medicationSelect.value === 'Yes') {
      medicationWrapper.style.display = 'block';
    } else {
      medicationWrapper.style.display = 'none';
      if (medicationInput) medicationInput.value = '';
    }
  }

  if (lifeConditionSelect) {
    lifeConditionSelect.addEventListener('change', toggleConditionDetails);
  }

  if (medicationSelect) {
    medicationSelect.addEventListener('change', toggleMedicationDetails);
  }

  // Run once on load (important for validation reloads)
  toggleConditionDetails();
  toggleMedicationDetails();
});
