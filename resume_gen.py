from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY

OUTPUT = "Resume_Samaranjan_Manjhi.pdf"

LM = 0.40 * inch
RM = 0.40 * inch

doc = SimpleDocTemplate(
    OUTPUT, pagesize=letter,
    leftMargin=LM, rightMargin=RM,
    topMargin=0.28 * inch, bottomMargin=0.25 * inch,
    title="Samaranjan Manjhi - Resume",
    author="Samaranjan Manjhi",
    subject="C/C++ Systems & Cyber Security Software Developer Resume",
    keywords="C++ Linux macOS systems programming cybersecurity security engineer DLP endpoint security kernel Qt Ed25519 OpenSSL SQLite"
)

# Usable content width
W = letter[0] - LM - RM - 12
DATE_W = 95.0
LEFT_W = W - DATE_W

BLACK = colors.black

def S(name, **kw): return ParagraphStyle(name, **kw)

# ── STYLES ─────────────────────────────────────────────
sName    = S("Name",    fontName="Times-Bold",    fontSize=20, textColor=BLACK, leading=19, alignment=TA_CENTER, spaceAfter=2)
sTitle   = S("Title",   fontName="Times-Bold",    fontSize=10, textColor=BLACK, leading=11, alignment=TA_CENTER, spaceAfter=2)
sContact = S("Contact", fontName="Times-Roman",   fontSize=8.8, textColor=BLACK, leading=10, alignment=TA_CENTER, spaceAfter=2.5)
sSection = S("Section", fontName="Times-Bold",    fontSize=10.5, textColor=BLACK, leading=10, spaceBefore=2.5, spaceAfter=1.6)
sSum     = S("Sum",     fontName="Times-Roman",   fontSize=9.0, textColor=BLACK, leading=10.7, alignment=TA_JUSTIFY, spaceAfter=1)
sBullet  = S("Bullet",  fontName="Times-Roman",   fontSize=8.8, textColor=BLACK, leading=10.1, leftIndent=8, firstLineIndent=-8, spaceAfter=0.8)
sInline  = S("Inline",  fontName="Times-Roman",   fontSize=8.8, textColor=BLACK, leading=10.2, spaceAfter=0)
sHdrL    = S("HdrL",    fontName="Times-Bold",    fontSize=10.2, textColor=BLACK, leading=10.8)
sHdrR    = S("HdrR",    fontName="Times-Italic",  fontSize=8.8, textColor=BLACK, leading=10.8, alignment=TA_RIGHT)
sEduT    = S("EduT",    fontName="Times-Bold",    fontSize=9.5, textColor=BLACK, leading=11, spaceBefore=0)
sEduM    = S("EduM",    fontName="Times-Roman",   fontSize=9.5, textColor=BLACK, leading=11)

BULLET = u"\u2022"

# ── HELPERS ─────────────────────────────────────────────
def rule():
    return HRFlowable(width="100%", thickness=0.6, color=BLACK, spaceAfter=1.2, spaceBefore=0.6)

def section(title):
    return [Paragraph(title.upper(), sSection), rule()]

def bullet(text):
    return Paragraph(f"{BULLET}  {text}", sBullet)

def skill_line(label, value):
    return Paragraph(f"<b>{label}:</b>  {value}", sInline)

def hdr_row(left_markup, date_str):
    t = Table(
        [[Paragraph(left_markup, sHdrL), Paragraph(date_str, sHdrR)]],
        colWidths=[LEFT_W, DATE_W],
        hAlign='LEFT'
    )
    t.setStyle(TableStyle([
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING",   (0,0), (-1,-1), 0),
        ("RIGHTPADDING",  (0,0), (-1,-1), 0),
        ("TOPPADDING",    (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ]))
    return t

def job_header(left, dates):
    return [hdr_row(left, dates)]

def proj_header(name, tech, dates):
    left = f"<b>{name}</b>  <font color='#444444' size='7.3'>|  {tech}</font>"
    return [Spacer(1, 0.6), hdr_row(left, dates)]

# ── STORY ─────────────────────────────────────────────
story = []

# Header Block
story.append(Paragraph("Samaranjan Manjhi", sName))
story.append(Paragraph("C/C++ Systems &amp; Cyber Security Software Developer", sTitle))
story.append(Paragraph(
    "+91 9082650120 | <a href='mailto:samaranjanedu01@gmail.com'>samaranjanedu01@gmail.com</a> "
    "| <a href='https://linkedin.com/in/samaranjan-manjhi'>LinkedIn</a> "
    "| <a href='https://samaranjan-manjhi.github.io/Resume/'>Portfolio (Video Demos)</a> "
    "| Mumbai, India", sContact))

# Summary
story += section("Summary")
story.append(Paragraph(
    "C/C++ Systems and Cyber Security Engineer with <b>3+ years</b> of experience building production-grade "
    "endpoint security tools, kernel monitors, binary integrity frameworks, and Data Loss Prevention (DLP) systems for "
    "<b>macOS and Linux</b>. Deep expertise in Endpoint Security Framework (ESF), "
    "execution gating, system call hooking, Qt GUI development, and cross-platform C++ architecture. "
    "Delivered <b>10+ enterprise security modules</b> deployed globally across macOS and Linux endpoints for enterprise antivirus suites.", sSum))

# Technical Skills
story += section("Technical Skills")
story.append(skill_line("Languages",  "C, C++, Bash Scripting, Relational SQL"))
story.append(skill_line("Frameworks", "Endpoint Security Framework (ESF), Extended Berkeley Packet Filter (eBPF), System Audit, Core Foundation"))
story.append(skill_line("Security",   "Cyber Security Architecture, Sodium Cryptography Library, OpenSSL Library"))
story.append(skill_line("Tools",      "Git, CMake, Make, Xcode, GDB, Valgrind, KDB/KGDB, SQLite, Boost, Nano"))
story.append(skill_line("Core CS",    "Data Structures, Multithreading, Inter-Process Communication, TCP/IP Networking, OS Internals (Linux/macOS)"))
story.append(Spacer(1, 1.5))

# Professional Experience
story += section("Professional Experience")
story += job_header(
    "<b>Systems &amp; Security Software Engineer</b>  <font color='black' size='7.8'>|  MicroWorld Software Services Pvt. Ltd. &mdash; Mumbai</font>",
    "Aug 2023 – Present")
story.append(bullet("Designed and delivered <b>10+ production security modules</b> spanning kernel monitors, DLP engines, binary integrity systems, firewall rule generators, and cloud backup agents — deployed globally across enterprise Linux and macOS systems running security products."))
story.append(bullet("Constructed high-performance cross-platform security daemons in C/C++, integrating Linux kernel modules, macOS ESF event loops, and POSIX Unix domain socket IPC to reduce system memory overhead by 25% and improve event detection throughput by 40%."))
story.append(bullet("Independently owned end-to-end design, implementation, and deployment for select modules, coordinating with QA and product teams to define requirements and validate detection accuracy prior to release."))
story.append(bullet("Regularly mentored and onboarded new engineers on secure C/C++ development, kernel-level debugging, and internal security frameworks, shortening ramp-up time on kernel and DLP module development."))
story.append(Spacer(1, 1.5))

# Key Projects
story += section("Key Projects")

story += proj_header("Real-Time Virus Scanning — eBPF", "C/C++, eBPF, Kernel Tracing, AV Engine Integration", "Mar 2026 – Jun 2026")
story.append(bullet("Built a real-time on-access antivirus scanning daemon using eBPF programs attached to kernel hooks to intercept file open, write, and execution events, streaming new and modified files into the AV scan engine for detection."))
story.append(bullet("Integrated quarantine and process-termination actions triggered on malware detection, with a configurable watchlist and root/parent-process validation to reduce false positives and redundant re-scans."))
story.append(bullet("Optimized event throughput with a lock-free audit map and dedicated scanner thread pool, sustaining real-time on-access detection under heavy file I/O without blocking user processes."))

story += proj_header("MW Guardian — Binary Integrity & Execution Gating", "C/C++, Linux Kernel, Cryptographic Verification", "Feb 2026 – Jul 2026")
story.append(bullet("Enforced execution gating via <b>kernel permission events</b> to intercept binary execution at kernel level, synchronously validating cryptographic signatures and terminating untrusted binaries prior to execution."))
story.append(bullet("Architected a multi-key cryptographic signing pipeline supporting key rotation while retaining legacy public keys to preserve signature validity for previously signed binaries."))
story.append(bullet("Created startup self-verification routines where guardian and verifier components validate their own binary signatures prior to initiating the main event loop, eliminating bootstrap trust gaps."))

story += proj_header("Two-Factor Authentication for SSH", "C/C++, PAM Module, TOTP Cryptography, Qt Framework, macOS", "Jul 2026 – Aug 2026")
story.append(bullet("Extended the PAM authentication stack with a custom TOTP verification module, layering a second authentication factor onto SSH login while preserving compatibility with existing PAM configuration and login flows."))
story.append(bullet("Built and integrated a Qt-based 2FA enrollment and management widget directly into the production macOS security console GUI, allowing administrators to enable, configure, and audit 2FA policy per endpoint."))
story.append(bullet("Implemented secret provisioning and QR-code based device enrollment, coordinating configuration state between the PAM module and GUI layer without requiring a service restart."))

story += proj_header("Printer Control & Data Loss Prevention (DLP)", "macOS, C/C++, ESF, Print Service Libraries, Xcode", "Oct 2025 – Jan 2026")
story.append(bullet("Developed a macOS DLP driver utilizing ESF and print spool monitoring to inspect print files for sensitive information, cancelling unauthorized print jobs prior to printing."))
story.append(bullet("Applied application-level process whitelisting and blacklisting enforced via ESF process identity, bypassing clean content for trusted applications and blocking unauthorized applications outright."))
story.append(bullet("Archived scanned print jobs alongside result metadata to maintain audit trails for compliance reporting and post-event forensic investigations."))

story += proj_header("File Integrity Monitoring (FIM)", "macOS, C/C++, File System Events, SQLite Database, CommonCrypto MD5", "Jun 2025 – Aug 2025")
story.append(bullet("Built a file system event daemon storing cryptographic file hashes, permissions, file sizes, and timestamps in SQLite, emitting real-time security alerts upon unauthorized path modifications, renames, or deletions."))
story.append(bullet("Established baseline state snapshots on initial startup and executed diff comparisons on subsequent runs to output structured security event logs across configurable watch paths."))

story += proj_header("Content Scanner — DLP Engine & CLI", "C/C++, Regex Engine, Optical Character Recognition, Archive Libraries", "Sep 2024 – May 2025")
story.append(bullet("Built a multi-threaded DLP scanner supporting <b>15+ file formats</b> via regular expression parsing and optical character recognition, packaged as a shared library and CLI utility."))
story.append(bullet("Developed a high-performance Unix domain socket server variant allowing clients to stream file paths and retrieve scan results without re-initializing regex engines, reducing per-scan latency by 60%."))

story.append(Spacer(1, 1.5))

# Education
story += section("Education")
story += job_header("<b>Bachelor of Engineering — Computer Engineering</b>", "2019 – 2023")
story.append(Paragraph(
    "Shree L.R. Tiwari College of Engineering, Mumbai University &mdash; CGPA: <b>8.56 / 10</b>",
    sEduM))

# Render document
doc.build(story)
print("Successfully generated ATS-optimized PDF:", OUTPUT)
