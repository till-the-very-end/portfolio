/* ==========================================================================
   Engineering Portfolio Logic
   Authentic, snappy, high-performance interactions
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Theme Management (Light / High-Contrast Dark)
  const themeToggle = document.getElementById('themeToggle');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const savedTheme = localStorage.getItem('portfolio-theme');

  if (savedTheme) {
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeLabel(savedTheme);
  } else if (prefersDark) {
    document.documentElement.setAttribute('data-theme', 'dark');
    updateThemeLabel('dark');
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme') || 'light';
      const target = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', target);
      localStorage.setItem('portfolio-theme', target);
      updateThemeLabel(target);
    });
  }

  function updateThemeLabel(theme) {
    if (!themeToggle) return;
    const label = themeToggle.querySelector('.theme-mode-label');
    if (label) {
      label.textContent = theme === 'dark' ? 'DARK' : 'LIGHT';
    }
  }

  // 2. Project Filtering
  const filterButtons = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');

  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      filterButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter');

      projectCards.forEach(card => {
        const category = card.getAttribute('data-category');
        if (filter === 'all' || category === filter) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  // 3. Interactive GRC Risk Calculator
  const assetSelect = document.getElementById('assetCriticality');
  const threatSelect = document.getElementById('threatLikelihood');
  const scoreDisplay = document.getElementById('riskScore');
  const recDisplay = document.getElementById('riskRec');

  function updateRiskCalc() {
    if (!assetSelect || !threatSelect || !scoreDisplay || !recDisplay) return;

    const assetVal = parseInt(assetSelect.value, 10);
    const threatVal = parseInt(threatSelect.value, 10);
    const score = assetVal * threatVal;

    scoreDisplay.className = 'score-badge';
    let levelText = '';
    let adviceText = '';

    if (score <= 3) {
      scoreDisplay.classList.add('score-low');
      levelText = 'LOW';
      adviceText = 'ISO 27001 A.8.1 (Asset Inventory) & periodic review. Standard baseline security controls sufficient.';
    } else if (score <= 6) {
      scoreDisplay.classList.add('score-med');
      levelText = 'MEDIUM';
      adviceText = 'NIST CSF PR.AC-1 & ISO 27001 A.9 (Access Control). Enforce role-based access control and semi-annual gap audits.';
    } else if (score <= 11) {
      scoreDisplay.classList.add('score-high');
      levelText = 'HIGH';
      adviceText = 'ISO 27001 A.12.6 (Vulnerability Management) & SOC 2 CC7.1. Implement vulnerability scanning (Nmap/Burp) and 30-day SLA remediation.';
    } else {
      scoreDisplay.classList.add('score-crit');
      levelText = 'CRITICAL';
      adviceText = 'Immediate escalation. Enforce multi-factor authentication, cryptographic data isolation (DPDP Act s.8), and daily audit log immutability.';
    }

    scoreDisplay.textContent = `${score} (${levelText})`;
    recDisplay.innerHTML = `<strong>Recommended Control Baseline:</strong> ${adviceText}`;
  }

  if (assetSelect && threatSelect) {
    assetSelect.addEventListener('change', updateRiskCalc);
    threatSelect.addEventListener('change', updateRiskCalc);
    updateRiskCalc();
  }

  // 4. Toast Notification
  const toast = document.getElementById('toast');
  function showToast(message) {
    if (!toast) return;
    toast.textContent = message;
    toast.style.display = 'block';
    setTimeout(() => {
      toast.style.display = 'none';
    }, 2800);
  }

  // 5. Copy Email
  const copyButtons = document.querySelectorAll('.btn-copy-email');
  copyButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const email = 'pknailkar@gmail.com';
      navigator.clipboard.writeText(email).then(() => {
        showToast('Email copied to clipboard: pknailkar@gmail.com');
      }).catch(() => {
        showToast('Email: pknailkar@gmail.com');
      });
    });
  });

  // 6. Resume Modal
  const resumeModal = document.getElementById('resumeModal');
  const openModalBtn = document.getElementById('openResumeModal');
  const closeModalBtn = document.getElementById('closeResumeModal');

  if (openModalBtn && resumeModal) {
    openModalBtn.addEventListener('click', (e) => {
      e.preventDefault();
      resumeModal.style.display = 'flex';
    });
  }

  if (closeModalBtn && resumeModal) {
    closeModalBtn.addEventListener('click', () => {
      resumeModal.style.display = 'none';
    });

    resumeModal.addEventListener('click', (e) => {
      if (e.target === resumeModal) {
        resumeModal.style.display = 'none';
      }
    });
  }

  // 7. Contact Form Simulation
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('senderName').value.trim();
      const email = document.getElementById('senderEmail').value.trim();
      const message = document.getElementById('senderMsg').value.trim();

      if (!name || !email || !message) {
        showToast('Please fill out all fields before sending.');
        return;
      }

      showToast(`Thank you, ${name}. Message prepared. Opening default mail client...`);
      const mailtoLink = `mailto:pknailkar@gmail.com?subject=Portfolio Inquiry from ${encodeURIComponent(name)}&body=${encodeURIComponent(message + "\n\nFrom: " + email)}`;
      window.location.href = mailtoLink;
      contactForm.reset();
    });
  }
});
