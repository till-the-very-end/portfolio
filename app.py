import streamlit as st
import os
import pandas as pd
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Prachi Kumar Nailkar - Cybersecurity & GRC Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-Contrast Engineering CSS
# Avoids AI tropes: Zero gradients, Zero Inter, Zero glowing borders, Clean 8px rhythm
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'IBM Plex Sans', -apple-system, sans-serif;
    color: #0f172a;
}

h1, h2, h3, h4 {
    font-family: 'IBM Plex Sans', sans-serif;
    color: #0f172a;
    font-weight: 600;
    letter-spacing: -0.02em;
}

.mono {
    font-family: 'IBM Plex Mono', monospace;
}

/* Card Styling: Crisp, structural, zero glassmorphism */
.eng-card {
    background-color: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 20px 24px;
    margin-bottom: 20px;
}

.eng-card-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 12px;
}

.eng-role {
    font-size: 1.15rem;
    font-weight: 600;
    color: #0f172a;
}

.eng-meta {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.8rem;
    color: #64748b;
}

.eng-tag {
    display: inline-block;
    background-color: #f1f5f9;
    color: #1e293b;
    border: 1px solid #cbd5e1;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.75rem;
    padding: 3px 8px;
    border-radius: 4px;
    margin-right: 6px;
    margin-bottom: 6px;
}

.status-badge {
    display: inline-flex;
    align-items: center;
    background-color: #ecfdf5;
    color: #15803d;
    border: 1px solid #a7f3d0;
    padding: 4px 10px;
    border-radius: 4px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.78rem;
    font-weight: 500;
    margin-bottom: 12px;
}

/* Hide default streamlit header decoration */
header[data-testid="stHeader"] {
    background: transparent;
}
</style>
""", unsafe_allow_html=True)

# Helper function to load resume binary
def load_resume_bytes():
    paths = ["Prachi_Kumar_Nailkar_Resume.pdf", "latest.pdf"]
    for p in paths:
        if os.path.exists(p):
            with open(p, "rb") as f:
                return f.read(), os.path.basename(p)
    return None, None

resume_bytes, resume_filename = load_resume_bytes()

# Sidebar: Identity & Quick Actions
with st.sidebar:
    # Profile Image
    if os.path.exists("profile.jpg"):
        image = Image.open("profile.jpg")
        st.image(image, use_container_width=True)
    
    st.markdown("### Prachi Kumar Nailkar")
    st.markdown("**Cybersecurity & GRC Engineering**")
    st.markdown("B.E. Computer Engineering (Class of 2027)  \nWadia College of Engineering, Pune")
    
    st.markdown("---")
    
    st.markdown("**Contact & Channels**")
    st.markdown("📍 Pune, Maharashtra, India")
    st.markdown("✉️ `pknailkar@gmail.com`")
    st.markdown("📞 `+91 7975010985`")
    st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/prachi-nailkar-85a024236)")
    st.markdown("[GitHub Repository](https://github.com/till-the-very-end)")
    
    st.markdown("---")
    
    if resume_bytes:
        st.download_button(
            label="Download Resume (PDF)",
            data=resume_bytes,
            file_name="Prachi_Kumar_Nailkar_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )

# Main Navigation Tabs
tab_overview, tab_experience, tab_projects, tab_calculator, tab_skills, tab_education, tab_contact = st.tabs([
    "Overview",
    "Experience",
    "Projects",
    "Interactive GRC Tool",
    "Technical Competencies",
    "Education & Certifications",
    "Contact"
])

# -----------------------------------------------------------------------------
# TAB 1: OVERVIEW
# -----------------------------------------------------------------------------
with tab_overview:
    st.markdown('<div class="status-badge">Available for Internships & Full-Time Security Roles</div>', unsafe_allow_html=True)
    st.title("Prachi Kumar Nailkar")
    st.subheader("Cybersecurity, GRC & Cloud Security Engineering")
    
    st.markdown("""
    Third-year Computer Engineering student at Modern Education Society's Wadia College of Engineering, Pune.
    Hands-on internship experience in vulnerability assessment, risk and control-gap identification, audit documentation,
    and compliance reporting across ISO 27001, SOC 2, NIST CSF, and the DPDP Act.
    
    Practical tooling in Burp Suite, Wireshark, Nmap, AWS Cloud, Python, and MongoDB.
    Skilled in translating technical security findings into clear, audit-ready documentation for both engineering teams and executive stakeholders.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        **Core Focus Areas**
        - Governance, Risk & Compliance (GRC)
        - Vulnerability Assessment & Recon
        - Cloud Security & Shared Responsibility
        """)
    with col2:
        st.markdown("""
        **Security Standards**
        - ISO/IEC 27001 (ISMS)
        - SOC 2 Type II Evidence
        - NIST Cybersecurity Framework
        - DPDP Act (India 2023)
        """)
    with col3:
        st.markdown("""
        **Engineering Arsenal**
        - Python (Security Scripting)
        - Wireshark, Nmap, Burp Suite
        - AWS Cloud Practitioner
        - Terraform & AWS SSM
        """)

# -----------------------------------------------------------------------------
# TAB 2: WORK EXPERIENCE
# -----------------------------------------------------------------------------
with tab_experience:
    st.header("Work Experience")
    
    # Role 1
    st.markdown("""
    <div class="eng-card">
        <div class="eng-card-header">
            <div>
                <div class="eng-role">Risk & Compliance Intern</div>
                <div style="color: #334155; font-weight: 500;">Uptoskills (Remote)</div>
            </div>
            <div class="eng-meta">Jan 2026 - Apr 2026</div>
        </div>
        <ul style="color: #334155; line-height: 1.7; margin-top: 10px;">
            <li>Prepared vulnerability assessment and compliance reports using Burp Suite, Nmap, and Nikto, documenting findings and remediation timelines.</li>
            <li>Supported risk and control-gap identification through security reconnaissance using WhatWeb, Wappalyzer, and Netcraft.</li>
            <li>Produced structured, audit-ready documentation aligned with ISO 27001 and SOC 2 evidence requirements.</li>
            <li>Translated technical findings into clear reports for non-technical stakeholders and organized remediation information for executive review.</li>
        </ul>
        <div style="margin-top: 12px;">
            <span class="eng-tag">ISO 27001</span>
            <span class="eng-tag">SOC 2</span>
            <span class="eng-tag">Burp Suite</span>
            <span class="eng-tag">Nmap</span>
            <span class="eng-tag">Nikto</span>
            <span class="eng-tag">Evidence Auditing</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Role 2
    st.markdown("""
    <div class="eng-card">
        <div class="eng-card-header">
            <div>
                <div class="eng-role">Cybersecurity & Compliance Intern</div>
                <div style="color: #334155; font-weight: 500;">Jyesta Corporate Entity (Pune, India)</div>
            </div>
            <div class="eng-meta">Oct 2025 - Dec 2025</div>
        </div>
        <ul style="color: #334155; line-height: 1.7; margin-top: 10px;">
            <li>Supported security audit readiness and compliance reviews by documenting 20+ security control findings in structured audit logs.</li>
            <li>Maintained audit documentation and security evidence repositories, ensuring findings were tagged and version-controlled for audit traceability.</li>
            <li>Translated technical network security findings using Wireshark and Nmap into clear policy documentation.</li>
        </ul>
        <div style="margin-top: 12px;">
            <span class="eng-tag">Control Logs</span>
            <span class="eng-tag">Wireshark</span>
            <span class="eng-tag">Nmap</span>
            <span class="eng-tag">Audit Traceability</span>
            <span class="eng-tag">Network Defense</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# TAB 3: SELECTED PROJECTS
# -----------------------------------------------------------------------------
with tab_projects:
    st.header("Selected Projects & Engineering Case Studies")
    
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        st.markdown("""
        <div class="eng-card">
            <span class="eng-meta" style="color: #0f3b60; font-weight: 600;">GOVERNANCE, RISK & COMPLIANCE</span>
            <h3 style="margin-top: 6px; margin-bottom: 8px;">FinTech GRC Automation (CoinFlow India)</h3>
            <p style="color: #334155; font-size: 0.92rem;">
                Developed a Python-based policy gap analysis framework mapping operational controls to Reserve Bank of India (RBI) guidelines and ISO 27001 requirements.
            </p>
            <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; padding: 10px; border-radius: 4px; margin: 12px 0;">
                <span class="mono" style="font-size: 0.75rem; color: #64748b; display: block;">ENGINEERING IMPACT</span>
                <strong style="color: #0f172a; font-size: 0.88rem;">Reduced manual audit effort by 40% through automated control checks.</strong>
            </div>
            <span class="eng-tag">Python</span>
            <span class="eng-tag">ISO 27001</span>
            <span class="eng-tag">RBI Norms</span>
            <span class="eng-tag">ISMS</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="eng-card">
            <span class="eng-meta" style="color: #0f3b60; font-weight: 600;">ZERO-TRUST AUDIT</span>
            <h3 style="margin-top: 6px; margin-bottom: 8px;">CyberGita: EdTech Security & Privacy Audit</h3>
            <p style="color: #334155; font-size: 0.92rem;">
                Conducted an ISMS-style security evaluation of learning platform architecture. Drafted a risk-prioritized remediation roadmap compliant with the DPDP Act and NIST CSF.
            </p>
            <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; padding: 10px; border-radius: 4px; margin: 12px 0;">
                <span class="mono" style="font-size: 0.75rem; color: #64748b; display: block;">FRAMEWORK ALIGNMENT</span>
                <strong style="color: #0f172a; font-size: 0.88rem;">Mapped 35+ control checkpoints across NIST CSF and DPDP Act provisions.</strong>
            </div>
            <span class="eng-tag">DPDP Act</span>
            <span class="eng-tag">NIST CSF</span>
            <span class="eng-tag">Access Control</span>
            <span class="eng-tag">Risk Roadmap</span>
        </div>
        """, unsafe_allow_html=True)

    with col_p2:
        st.markdown("""
        <div class="eng-card">
            <span class="eng-meta" style="color: #0f3b60; font-weight: 600;">CLOUD SECURITY & AUTOMATION</span>
            <h3 style="margin-top: 6px; margin-bottom: 8px;">SOAR Infrastructure & Adversary Simulation</h3>
            <p style="color: #334155; font-size: 0.92rem;">
                Engineered automated attack simulation and verification pipelines on AWS. Deployed Sandcat/Caldera adversary profiles via AWS Systems Manager (SSM) to test detection accuracy and persistence.
            </p>
            <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; padding: 10px; border-radius: 4px; margin: 12px 0;">
                <span class="mono" style="font-size: 0.75rem; color: #64748b; display: block;">AUTOMATION PIPELINE</span>
                <strong style="color: #0f172a; font-size: 0.88rem;">Terraform IaC, PowerShell execution engine, AWS SSM remote orchestrator.</strong>
            </div>
            <span class="eng-tag">Terraform</span>
            <span class="eng-tag">AWS SSM</span>
            <span class="eng-tag">Sandcat</span>
            <span class="eng-tag">Incident Response</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="eng-card">
            <span class="eng-meta" style="color: #0f3b60; font-weight: 600;">MACHINE LEARNING / APPSEC</span>
            <h3 style="margin-top: 6px; margin-bottom: 8px;">AI Phishing Email Classifier</h3>
            <p style="color: #334155; font-size: 0.92rem;">
                Developed and deployed a machine-learning phishing email classifier using Python and joblib with probability confidence scoring for suspicious email payloads.
            </p>
            <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; padding: 10px; border-radius: 4px; margin: 12px 0;">
                <span class="mono" style="font-size: 0.75rem; color: #64748b; display: block;">DEPLOYMENT</span>
                <strong style="color: #0f172a; font-size: 0.88rem;">Interactive Python Streamlit web frontend with serialized scikit-learn model.</strong>
            </div>
            <span class="eng-tag">Python</span>
            <span class="eng-tag">Scikit-Learn</span>
            <span class="eng-tag">Joblib</span>
            <span class="eng-tag">Streamlit</span>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# TAB 4: INTERACTIVE GRC RISK TOOL
# -----------------------------------------------------------------------------
with tab_calculator:
    st.header("Interactive GRC Risk Scoring Calculator")
    st.markdown("""
    This interactive calculator demonstrates quantitative risk scoring and control mapping 
    aligned with **ISO/IEC 27001:2022** and **NIST CSF** risk assessment methodology.
    """)
    
    calc_col1, calc_col2 = st.columns(2)
    
    with calc_col1:
        asset_crit = st.selectbox(
            "Asset Criticality (Impact Score)",
            options=[
                (1, "1 - Low: Non-critical internal assets, public documentation"),
                (2, "2 - Medium: Internal operational tools, business logs"),
                (3, "3 - High: Production application data, employee PII"),
                (4, "4 - Critical: Master customer credentials, financial core")
            ],
            format_func=lambda x: x[1],
            index=2
        )
        
        threat_prob = st.selectbox(
            "Threat Likelihood (Probability Score)",
            options=[
                (1, "1 - Rare: Air-gapped, zero external network interface"),
                (2, "2 - Moderate: Internal corporate network, authenticated users"),
                (3, "3 - Likely: Internet exposed API, public domain DNS"),
                (4, "4 - Frequent: Active CVE on public perimeter, targeted surface")
            ],
            format_func=lambda x: x[1],
            index=1
        )
    
    impact = asset_crit[0]
    prob = threat_prob[0]
    score = impact * prob
    
    with calc_col2:
        st.markdown("**Calculated Risk Assessment**")
        if score <= 3:
            st.success(f"Risk Score: {score}/16 - LOW RISK")
            st.markdown("""
            **Recommended ISO 27001 / NIST Controls:**
            - **ISO 27001 A.8.1**: Asset inventory & annual classification review.
            - **NIST CSF ID.AM-1**: Physical and software systems cataloged.
            - Baseline security hygiene is sufficient.
            """)
        elif score <= 6:
            st.info(f"Risk Score: {score}/16 - MEDIUM RISK")
            st.markdown("""
            **Recommended ISO 27001 / NIST Controls:**
            - **ISO 27001 A.9**: User Access Management & least-privilege review.
            - **NIST CSF PR.AC-1**: Identities and credentials managed.
            - Semi-annual access recertification and quarterly log reviews.
            """)
        elif score <= 11:
            st.warning(f"Risk Score: {score}/16 - HIGH RISK")
            st.markdown("""
            **Recommended ISO 27001 / NIST Controls:**
            - **ISO 27001 A.12.6**: Management of technical vulnerabilities.
            - **SOC 2 CC7.1**: Vulnerability scanning (Burp Suite, Nmap) with 30-day SLA remediation.
            - Mandatory multi-factor authentication (MFA) and encrypted backups.
            """)
        else:
            st.error(f"Risk Score: {score}/16 - CRITICAL RISK")
            st.markdown("""
            **Recommended ISO 27001 / NIST Controls:**
            - **Immediate Escalation**: Executive risk acceptance or immediate containment.
            - **DPDP Act s.8**: Cryptographic isolation for sensitive personal data.
            - Immutable audit logging, daily penetration tests, and automated incident runbooks.
            """)

# -----------------------------------------------------------------------------
# TAB 5: TECHNICAL COMPETENCIES MATRIX
# -----------------------------------------------------------------------------
with tab_skills:
    st.header("Technical Competencies Matrix")
    
    sk1, sk2, sk3, sk4 = st.columns(4)
    
    with sk1:
        st.markdown("#### Cloud & Systems")
        df_cloud = pd.DataFrame({
            "Technology": ["AWS Cloud Practitioner", "AWS SSM", "Shared Responsibility", "MongoDB CRUD", "SQL Relational", "Linux CLI / Bash"],
            "Proficiency": ["Certified", "Applied", "Core", "Working", "Basic", "Proficient"]
        })
        st.table(df_cloud)

    with sk2:
        st.markdown("#### GRC & Frameworks")
        df_grc = pd.DataFrame({
            "Framework": ["ISO/IEC 27001", "SOC 2 Type II", "NIST CSF", "DPDP Act (India)", "Control-Gap Review", "Audit Evidence Logs"],
            "Proficiency": ["Core", "Audit-Ready", "Applied", "Regulatory", "Proficient", "Practical"]
        })
        st.table(df_grc)

    with sk3:
        st.markdown("#### Security & Recon Tools")
        df_tools = pd.DataFrame({
            "Tool": ["Wireshark", "Burp Suite", "Nmap", "Nikto", "WhatWeb / Wappalyzer", "SSLScan / Netcraft"],
            "Proficiency": ["Advanced", "Practical", "Proficient", "Hands-on", "Recon", "Applied"]
        })
        st.table(df_tools)

    with sk4:
        st.markdown("#### Languages & Tooling")
        df_lang = pd.DataFrame({
            "Tool / Language": ["Python 3", "PowerShell", "Java", "Git / GitHub", "Streamlit", "Technical Documentation"],
            "Proficiency": ["Primary", "Automation", "Basic", "Versioned", "Frontend", "Audited"]
        })
        st.table(df_lang)

# -----------------------------------------------------------------------------
# TAB 6: EDUCATION & CERTIFICATIONS
# -----------------------------------------------------------------------------
with tab_education:
    st.header("Education & Certifications")
    
    ed_col1, ed_col2 = st.columns(2)
    
    with ed_col1:
        st.subheader("Academic Background")
        st.markdown("""
        **Modern Education Society's Wadia College of Engineering (Pune, India)**  
        *Bachelor of Engineering (B.E.), Computer Engineering - 3rd Year*  
        Expected Graduation: 2027  
        Focus: Network security, operating systems, database management systems, data structures.
        
        **Bangalore International Academy (Bengaluru, India)**  
        *Pre-University Education (PCMB)*  
        
        **Christ School ICSE, SG Palya (Bengaluru, India)**  
        *Secondary Education (ICSE Curriculum)*
        """)
        
        st.subheader("Honors & Leadership")
        st.markdown("""
        - **Best Volunteer Award**: NSS Unit, Wadia College of Engineering.
        - **Smart India Hackathon (SIH)**: National Level Participant.
        - **PR Head**: Nakshatra Astronomy Club (led student outreach and campus symposiums).
        """)

    with ed_col2:
        st.subheader("Verified Certifications")
        st.markdown("""
        - **AWS Cloud Practitioner Essentials** - AWS Training & Certification (Oct 2026)
        - **MongoDB CRUD Operations: Replace and Delete Documents** - MongoDB University (Jun 2025)
        - **Cybersecurity Analyst Professional** - IBM / Coursera
        - **Cybersecurity Job Simulation** - Forage
        - **Networking Basics** - Infosys Springboard
        - **Java Basics Aptitude** - Technical Assessment
        - **ChatGPT for Everyone** - Guvi HCL
        """)

# -----------------------------------------------------------------------------
# TAB 7: CONTACT
# -----------------------------------------------------------------------------
with tab_contact:
    st.header("Contact & Inquiries")
    st.markdown("""
    Open to internship and entry-level positions in Cloud Security, Security Analyst, and GRC domains.
    """)
    
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email Address")
        subject = st.text_input("Subject", value="Portfolio Inquiry / Security Opportunity")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send Inquiry")
        
        if submitted:
            if name and email and message:
                st.success(f"Thank you, {name}! Your inquiry has been registered. You can also email directly at pknailkar@gmail.com.")
            else:
                st.warning("Please fill out all required fields.")
