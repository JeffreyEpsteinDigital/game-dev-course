import json
import os
from datetime import datetime
from typing import Dict, List, Optional

class PortfolioGenerator:
    """Generate a complete personal portfolio website"""
    
    def __init__(self, config_file: Optional[str] = None):
        """
        Initialize portfolio generator
        
        Args:
            config_file: Path to JSON configuration file (optional)
        """
        if config_file and os.path.exists(config_file):
            with open(config_file, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        else:
            self.config = self.get_default_config()
    
    def get_default_config(self) -> Dict:
        """Return default portfolio configuration"""
        return {
            "personal_info": {
                "name": "Alex Johnson",
                "title": "Full Stack Developer & Data Scientist",
                "email": "alex.johnson@example.com",
                "phone": "+1 (555) 123-4567",
                "location": "San Francisco, CA",
                "website": "www.alexjohnson.dev",
                "photo_url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop",
                "bio": "Passionate developer with 5+ years of experience building scalable web applications and data-driven solutions. Love solving complex problems and creating impactful software.",
                "summary": "I specialize in Python, JavaScript, and cloud technologies, with a focus on creating efficient, user-friendly applications."
            },
            "social_links": {
                "GitHub": "https://github.com/alexjohnson",
                "LinkedIn": "https://linkedin.com/in/alexjohnson",
                "Twitter": "https://twitter.com/alexjohnson",
                "Instagram": "https://instagram.com/alexjohnson"
            },
            "skills": {
                "Programming": ["Python", "JavaScript", "TypeScript", "Java"],
                "Web Development": ["React", "Vue.js", "Django", "Flask", "FastAPI"],
                "Databases": ["PostgreSQL", "MySQL", "MongoDB", "Redis"],
                "DevOps & Cloud": ["Docker", "Kubernetes", "AWS", "Git", "CI/CD"],
                "Data Science": ["Pandas", "NumPy", "Scikit-learn", "TensorFlow"]
            },
            "experience": [
                {
                    "title": "Senior Software Engineer",
                    "company": "Tech Innovations Inc.",
                    "location": "San Francisco, CA",
                    "period": "2022 - Present",
                    "description": "Lead development of microservices architecture, improved system performance by 40%, mentored junior developers, implemented CI/CD pipelines.",
                    "achievements": ["Reduced API response time by 60%", "Increased test coverage to 90%", "Led migration to cloud infrastructure"]
                },
                {
                    "title": "Full Stack Developer",
                    "company": "Digital Solutions Ltd.",
                    "location": "New York, NY",
                    "period": "2020 - 2022",
                    "description": "Developed and maintained multiple web applications, collaborated with design teams, implemented responsive designs.",
                    "achievements": ["Built 10+ client projects", "Improved site performance scores", "Implemented automated testing"]
                }
            ],
            "education": [
                {
                    "degree": "Master of Science in Computer Science",
                    "institution": "Stanford University",
                    "location": "Stanford, CA",
                    "period": "2018 - 2020",
                    "gpa": "3.8/4.0"
                },
                {
                    "degree": "Bachelor of Software Engineering",
                    "institution": "MIT",
                    "location": "Cambridge, MA",
                    "period": "2014 - 2018",
                    "gpa": "3.9/4.0"
                }
            ],
            "projects": [
                {
                    "name": "E-commerce Platform",
                    "description": "Full-stack e-commerce solution with payment integration and inventory management",
                    "technologies": ["Django", "React", "PostgreSQL", "Stripe API"],
                    "link": "https://github.com/alexjohnson/ecommerce",
                    "github": "https://github.com/alexjohnson/ecommerce"
                },
                {
                    "name": "Task Management App",
                    "description": "Productivity application with real-time collaboration features",
                    "technologies": ["FastAPI", "Vue.js", "WebSockets", "Redis"],
                    "link": "https://taskapp.demo.com",
                    "github": "https://github.com/alexjohnson/taskapp"
                },
                {
                    "name": "Weather Dashboard",
                    "description": "Real-time weather monitoring dashboard with analytics",
                    "technologies": ["Python", "JavaScript", "Chart.js", "OpenWeather API"],
                    "link": "https://weather.alexjohnson.dev",
                    "github": "https://github.com/alexjohnson/weather-dash"
                }
            ],
            "certifications": [
                "AWS Certified Solutions Architect",
                "Google Professional Data Engineer",
                "Python Institute PCAP",
                "Docker Certified Associate"
            ],
            "languages": [
                {"name": "English", "level": "Native"},
                {"name": "Spanish", "level": "Fluent"},
                {"name": "French", "level": "Intermediate"}
            ],
            "style": {
                "theme": "dark",  # "dark" or "light"
                "primary_color": "#3B82F6",
                "secondary_color": "#10B981",
                "accent_color": "#8B5CF6"
            }
        }
    
    def generate_css(self) -> str:
        """Generate CSS styles based on configuration"""
        theme = self.config["style"]["theme"]
        primary = self.config["style"]["primary_color"]
        secondary = self.config["style"]["secondary_color"]
        accent = self.config["style"]["accent_color"]
        
        if theme == "dark":
            bg_color = "#0F172A"
            text_color = "#F1F5F9"
            card_bg = "#1E293B"
            border_color = "#334155"
        else:
            bg_color = "#FFFFFF"
            text_color = "#1F2937"
            card_bg = "#F8FAFC"
            border_color = "#E5E7EB"
        
        return f'''
        /* Generated Portfolio CSS */
        :root {{
            --primary: {primary};
            --secondary: {secondary};
            --accent: {accent};
            --bg-color: {bg_color};
            --text-color: {text_color};
            --card-bg: {card_bg};
            --border-color: {border_color};
        }}
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background: var(--bg-color);
            min-height: 100vh;
            transition: all 0.3s ease;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }}
        
        /* Header & Navigation */
        header {{
            padding: 40px 0;
            text-align: center;
            border-bottom: 1px solid var(--border-color);
        }}
        
        .profile-section {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px;
        }}
        
        .profile-image {{
            width: 200px;
            height: 200px;
            border-radius: 50%;
            object-fit: cover;
            border: 5px solid var(--primary);
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }}
        
        .name {{
            font-size: 3.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }}
        
        .title {{
            font-size: 1.5rem;
            color: var(--secondary);
            margin-bottom: 20px;
        }}
        
        .social-links {{
            display: flex;
            gap: 20px;
            justify-content: center;
            flex-wrap: wrap;
        }}
        
        .social-link {{
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 10px 20px;
            background: var(--card-bg);
            border-radius: 50px;
            text-decoration: none;
            color: var(--text-color);
            border: 1px solid var(--border-color);
            transition: all 0.3s ease;
        }}
        
        .social-link:hover {{
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            border-color: var(--primary);
        }}
        
        /* Main Content */
        main {{
            padding: 60px 0;
        }}
        
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
            margin-bottom: 60px;
        }}
        
        .card {{
            background: var(--card-bg);
            border-radius: 20px;
            padding: 30px;
            border: 1px solid var(--border-color);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        
        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        }}
        
        .card-title {{
            font-size: 1.8rem;
            margin-bottom: 25px;
            color: var(--primary);
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        
        .card-title::before {{
            content: '';
            width: 40px;
            height: 4px;
            background: var(--primary);
            border-radius: 2px;
        }}
        
        /* Skills */
        .skills-category {{
            margin-bottom: 25px;
        }}
        
        .category-title {{
            color: var(--secondary);
            margin-bottom: 10px;
            font-weight: 600;
        }}
        
        .skill-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }}
        
        .skill-tag {{
            background: linear-gradient(135deg, var(--primary), var(--accent));
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 500;
        }}
        
        /* Experience & Education */
        .timeline-item {{
            margin-bottom: 30px;
            padding-left: 30px;
            border-left: 3px solid var(--primary);
            position: relative;
        }}
        
        .timeline-item::before {{
            content: '';
            position: absolute;
            left: -10px;
            top: 0;
            width: 20px;
            height: 20px;
            background: var(--primary);
            border-radius: 50%;
        }}
        
        .item-title {{
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 5px;
        }}
        
        .item-subtitle {{
            color: var(--secondary);
            margin-bottom: 10px;
        }}
        
        .item-period {{
            display: inline-block;
            background: var(--accent);
            color: white;
            padding: 3px 10px;
            border-radius: 15px;
            font-size: 0.85rem;
            margin-bottom: 10px;
        }}
        
        /* Projects */
        .project-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
        }}
        
        .project-card {{
            background: var(--card-bg);
            border-radius: 15px;
            overflow: hidden;
            border: 1px solid var(--border-color);
            transition: all 0.3s ease;
        }}
        
        .project-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        }}
        
        .project-content {{
            padding: 25px;
        }}
        
        .project-title {{
            font-size: 1.4rem;
            margin-bottom: 10px;
            color: var(--primary);
        }}
        
        .project-tech {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin: 15px 0;
        }}
        
        .tech-tag {{
            background: var(--border-color);
            padding: 4px 12px;
            border-radius: 15px;
            font-size: 0.85rem;
        }}
        
        .project-links {{
            display: flex;
            gap: 15px;
            margin-top: 20px;
        }}
        
        .project-link {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            background: var(--primary);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            transition: all 0.3s ease;
        }}
        
        .project-link:hover {{
            background: var(--secondary);
            transform: scale(1.05);
        }}
        
        /* Contact */
        .contact-info {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }}
        
        .contact-item {{
            display: flex;
            align-items: center;
            gap: 15px;
            padding: 20px;
            background: var(--card-bg);
            border-radius: 12px;
            border: 1px solid var(--border-color);
        }}
        
        .contact-icon {{
            width: 40px;
            height: 40px;
            background: var(--primary);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
        }}
        
        /* Footer */
        footer {{
            text-align: center;
            padding: 40px 0;
            border-top: 1px solid var(--border-color);
            color: var(--text-color);
            opacity: 0.8;
        }}
        
        /* Responsive */
        @media (max-width: 768px) {{
            .name {{
                font-size: 2.5rem;
            }}
            
            .grid {{
                grid-template-columns: 1fr;
            }}
            
            .project-grid {{
                grid-template-columns: 1fr;
            }}
            
            .social-links {{
                flex-direction: column;
                align-items: center;
            }}
            
            .social-link {{
                width: 100%;
                max-width: 300px;
                justify-content: center;
            }}
        }}
        
        /* Animations */
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        .card, .project-card, .timeline-item {{
            animation: fadeIn 0.6s ease-out;
        }}
        
        /* Dark/Light mode toggle */
        .theme-toggle {{
            position: fixed;
            top: 20px;
            right: 20px;
            width: 50px;
            height: 50px;
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            z-index: 1000;
            transition: all 0.3s ease;
        }}
        
        .theme-toggle:hover {{
            transform: rotate(30deg);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }}
        '''
    
    def generate_html(self) -> str:
        """Generate complete HTML portfolio"""
        
        # Generate social links HTML
        social_html = ''
        for platform, url in self.config["social_links"].items():
            social_html += f'''
            <a href="{url}" class="social-link" target="_blank" rel="noopener">
                <span>{platform}</span>
            </a>'''
        
        # Generate skills HTML
        skills_html = ''
        for category, skill_list in self.config["skills"].items():
            skill_tags = ''.join([f'<span class="skill-tag">{skill}</span>' for skill in skill_list])
            skills_html += f'''
            <div class="skills-category">
                <h3 class="category-title">{category}</h3>
                <div class="skill-tags">
                    {skill_tags}
                </div>
            </div>'''
        
        # Generate experience HTML
        experience_html = ''
        for exp in self.config["experience"]:
            achievements = ''.join([f'<li>{achievement}</li>' for achievement in exp.get("achievements", [])])
            experience_html += f'''
            <div class="timeline-item">
                <span class="item-period">{exp["period"]}</span>
                <h3 class="item-title">{exp["title"]}</h3>
                <p class="item-subtitle">{exp["company"]} • {exp.get("location", "")}</p>
                <p>{exp["description"]}</p>
                {f'<ul>{achievements}</ul>' if achievements else ''}
            </div>'''
        
        # Generate education HTML
        education_html = ''
        for edu in self.config["education"]:
            education_html += f'''
            <div class="timeline-item">
                <span class="item-period">{edu["period"]}</span>
                <h3 class="item-title">{edu["degree"]}</h3>
                <p class="item-subtitle">{edu["institution"]} • {edu.get("location", "")}</p>
                {f'<p>GPA: {edu.get("gpa", "")}</p>' if edu.get("gpa") else ''}
            </div>'''
        
        # Generate projects HTML
        projects_html = ''
        for project in self.config["projects"]:
            tech_tags = ''.join([f'<span class="tech-tag">{tech}</span>' for tech in project["technologies"]])
            projects_html += f'''
            <div class="project-card">
                <div class="project-content">
                    <h3 class="project-title">{project["name"]}</h3>
                    <p>{project["description"]}</p>
                    <div class="project-tech">
                        {tech_tags}
                    </div>
                    <div class="project-links">
                        {f'<a href="{project["link"]}" class="project-link" target="_blank">🌐 Live Demo</a>' if project.get("link") else ''}
                        {f'<a href="{project["github"]}" class="project-link" target="_blank">💻 GitHub</a>' if project.get("github") else ''}
                    </div>
                </div>
            </div>'''
        
        # Generate certifications HTML
        certs_html = ''
        if "certifications" in self.config:
            for cert in self.config["certifications"]:
                certs_html += f'<div class="skill-tag">{cert}</div>'
        
        # Generate languages HTML
        languages_html = ''
        if "languages" in self.config:
            for lang in self.config["languages"]:
                languages_html += f'''
                <div class="skill-tag">
                    {lang["name"]} <span style="opacity: 0.8;">({lang["level"]})</span>
                </div>'''
        
        # Generate contact HTML
        contact_html = ''
        contact_info = self.config["personal_info"]
        contact_items = [
            ("📧", "Email", f"mailto:{contact_info['email']}", contact_info['email']),
            ("📱", "Phone", f"tel:{contact_info['phone']}", contact_info['phone']),
            ("📍", "Location", "#", contact_info['location']),
            ("🌐", "Website", contact_info['website'], contact_info['website'])
        ]
        
        for icon, label, link, value in contact_items:
            contact_html += f'''
            <a href="{link}" class="contact-item" {'target="_blank"' if link != '#' else ''}>
                <div class="contact-icon">{icon}</div>
                <div>
                    <strong>{label}</strong>
                    <p>{value}</p>
                </div>
            </a>'''
        
        # Main HTML template
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.config["personal_info"]["name"]} - Portfolio</title>
    <meta name="description" content="Personal portfolio of {self.config["personal_info"]["name"]} - {self.config["personal_info"]["title"]}">
    <meta name="keywords" content="portfolio, developer, {self.config["personal_info"]["title"]}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        {self.generate_css()}
    </style>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>👨‍💻</text></svg>">
</head>
<body>
    <div class="theme-toggle" id="themeToggle">
        <i class="fas fa-moon"></i>
    </div>
    
    <div class="container">
        <header>
            <div class="profile-section">
                <img src="{self.config["personal_info"]["photo_url"]}" 
                     alt="{self.config["personal_info"]["name"]}" 
                     class="profile-image">
                <h1 class="name">{self.config["personal_info"]["name"]}</h1>
                <p class="title">{self.config["personal_info"]["title"]}</p>
                <p>{self.config["personal_info"]["bio"]}</p>
                <div class="social-links">
                    {social_html}
                </div>
            </div>
        </header>
        
        <main>
            <div class="grid">
                <!-- Skills Section -->
                <section class="card">
                    <h2 class="card-title">
                        <i class="fas fa-code"></i> Skills & Technologies
                    </h2>
                    {skills_html}
                    
                    {f'<h3 class="category-title" style="margin-top: 30px;">Certifications</h3><div class="skill-tags">{certs_html}</div>' if certs_html else ''}
                    
                    {f'<h3 class="category-title" style="margin-top: 30px;">Languages</h3><div class="skill-tags">{languages_html}</div>' if languages_html else ''}
                </section>
                
                <!-- About Section -->
                <section class="card">
                    <h2 class="card-title">
                        <i class="fas fa-user"></i> About Me
                    </h2>
                    <p>{self.config["personal_info"]["summary"]}</p>
                    <div style="margin-top: 30px;">
                        <h3 class="category-title">Quick Facts</h3>
                        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; margin-top: 15px;">
                            <div class="skill-tag">📍 {self.config["personal_info"]["location"]}</div>
                            <div class="skill-tag">🎓 {len(self.config["education"])} Degrees</div>
                            <div class="skill-tag">💼 {len(self.config["experience"])} Years Exp</div>
                            <div class="skill-tag">🚀 {len(self.config["projects"])} Projects</div>
                        </div>
                    </div>
                </section>
            </div>
            
            <!-- Experience Section -->
            <section class="card" style="margin-bottom: 30px;">
                <h2 class="card-title">
                    <i class="fas fa-briefcase"></i> Work Experience
                </h2>
                {experience_html}
            </section>
            
            <!-- Education Section -->
            <section class="card" style="margin-bottom: 30px;">
                <h2 class="card-title">
                    <i class="fas fa-graduation-cap"></i> Education
                </h2>
                {education_html}
            </section>
            
            <!-- Projects Section -->
            <section class="card" style="margin-bottom: 30px;">
                <h2 class="card-title">
                    <i class="fas fa-project-diagram"></i> Projects
                </h2>
                <div class="project-grid">
                    {projects_html}
                </div>
            </section>
            
            <!-- Contact Section -->
            <section class="card">
                <h2 class="card-title">
                    <i class="fas fa-envelope"></i> Contact Me
                </h2>
                <div class="contact-info">
                    {contact_html}
                </div>
                <div style="margin-top: 30px; text-align: center;">
                    <p>Feel free to reach out for collaborations or just a friendly hello! 👋</p>
                </div>
            </section>
        </main>
        
        <footer>
            <p>© {datetime.now().year} {self.config["personal_info"]["name"]}. All rights reserved.</p>
            <p style="margin-top: 10px; font-size: 0.9em; opacity: 0.7;">
                Portfolio generated with Python • Last updated: {datetime.now().strftime("%B %d, %Y")}
            </p>
        </footer>
    </div>
    
    <script>
        // Theme toggle functionality
        const themeToggle = document.getElementById('themeToggle');
        const themeIcon = themeToggle.querySelector('i');
        
        themeToggle.addEventListener('click', () => {{
            document.body.classList.toggle('light-mode');
            
            if (document.body.classList.contains('light-mode')) {{
                themeIcon.className = 'fas fa-sun';
                document.documentElement.style.setProperty('--bg-color', '#FFFFFF');
                document.documentElement.style.setProperty('--text-color', '#1F2937');
                document.documentElement.style.setProperty('--card-bg', '#F8FAFC');
                document.documentElement.style.setProperty('--border-color', '#E5E7EB');
            }} else {{
                themeIcon.className = 'fas fa-moon';
                document.documentElement.style.setProperty('--bg-color', '#0F172A');
                document.documentElement.style.setProperty('--text-color', '#F1F5F9');
                document.documentElement.style.setProperty('--card-bg', '#1E293B');
                document.documentElement.style.setProperty('--border-color', '#334155');
            }}
        }});
        
        // Smooth scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{
                        behavior: 'smooth'
                    }});
                }}
            }});
        }});
        
        // Animation on scroll
        const observerOptions = {{
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        }};
        
        const observer = new IntersectionObserver((entries) => {{
            entries.forEach(entry => {{
                if (entry.isIntersecting) {{
                    entry.target.style.animationPlayState = 'running';
                    observer.unobserve(entry.target);
                }}
            }});
        }}, observerOptions);
        
        document.querySelectorAll('.card, .project-card, .timeline-item').forEach(el => {{
            el.style.animationPlayState = 'paused';
            observer.observe(el);
        }});
    </script>
</body>
</html>'''
        
        return html
    
    def save_portfolio(self, filename: str = "portfolio.html"):
        """
        Save portfolio to HTML file
        
        Args:
            filename: Output filename
        """
        html = self.generate_html()
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ Portfolio successfully generated: {filename}")
        print(f"📁 Open {filename} in your browser to view it.")
        
        # Also save configuration for future editing
        config_filename = filename.replace('.html', '_config.json')
        with open(config_filename, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
        print(f"📄 Configuration saved: {config_filename}")
    
    def edit_config_interactively(self):
        """Interactive configuration editor"""
        print("🎨 Portfolio Configuration Editor")
        print("=" * 40)
        
        personal = self.config["personal_info"]
        
        personal["name"] = input(f"Your name [{personal['name']}]: ") or personal["name"]
        personal["title"] = input(f"Your title [{personal['title']}]: ") or personal["title"]
        personal["email"] = input(f"Your email [{personal['email']}]: ") or personal["email"]
        personal["phone"] = input(f"Your phone [{personal['phone']}]: ") or personal["phone"]
        personal["location"] = input(f"Your location [{personal['location']}]: ") or personal["location"]
        personal["website"] = input(f"Your website [{personal['website']}]: ") or personal["website"]
        personal["bio"] = input(f"Your bio (press Enter to keep): ") or personal["bio"]
        
        print("\n✅ Configuration updated!")
        return self.config


# Command Line Interface
def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate a personal portfolio website")
    parser.add_argument("--config", "-c", help="Path to configuration JSON file")
    parser.add_argument("--output", "-o", default="portfolio.html", help="Output HTML filename")
    parser.add_argument("--edit", "-e", action="store_true", help="Edit configuration interactively")
    parser.add_argument("--quick", "-q", action="store_true", help="Quick generate with defaults")
    
    args = parser.parse_args()
    
    if args.quick:
        # Quick generation with sample data
        generator = PortfolioGenerator()
        generator.save_portfolio(args.output)
    else:
        generator = PortfolioGenerator(args.config)
        
        if args.edit:
            generator.edit_config_interactively()
        
        generator.save_portfolio(args.output)


# Example usage
if __name__ == "__main__":
    # Simple usage
    generator = PortfolioGenerator()
    generator.save_portfolio("my_portfolio.html")
    
    # Or use command line: python portfolio_generator.py --output "alex_portfolio.html"
    
    print("\n🌟 Next steps:")
    print("1. Edit the generated HTML file or _config.json to add your information")
    print("2. Replace the photo URL with your own image")
    print("3. Add your real projects, experience, and skills")
    print("4. Customize colors and theme in the config")
    print("5. Host it on GitHub Pages or any web server")


