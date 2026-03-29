import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

better_chrome_css = r'''
        .chrome-text, h1, h2, p, .subtitle, .disclaimer, .phone, .quote {
            background: linear-gradient(to bottom right, #f8fafc 0%, #9ca3af 30%, #ffffff 50%, #64748b 70%, #cbd5e1 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent !important;
            text-shadow: 0px 1px 2px rgba(0,0,0,0.5);
        }

        /* Override links */
        .menu-item, .btn-enter, .btn-back {
            background: linear-gradient(to bottom right, #e2e8f0 0%, #9ca3af 45%, #ffffff 50%, #475569 55%, #cbd5e1 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent !important;
            text-shadow: 0px 1px 2px rgba(0,0,0,0.5);
            border-color: #94a3b8;
        }
        
        .menu-item:hover, .btn-enter:hover, .btn-back:hover {
            background: linear-gradient(to bottom right, #ffffff 0%, #cbd5e1 45%, #64748b 50%, #ffffff 55%, #e2e8f0 100%);
            -webkit-background-clip: text;
            background-clip: text;
            text-shadow: 0px 0px 15px rgba(255,255,255,0.6);
            color: transparent !important;
            border-color: #ffffff;
        }
'''

for f_name in html_files:
    with open(f_name, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(r'body, p, h1, h2, a, div, span, \.disclaimer, \.bio-content, \.quote\s*\{\s*color: transparent;\s*\}', '', content)
    content = re.sub(r'\.chrome-text\s*\{.*?</style>', better_chrome_css + '\n    </style>', content, flags=re.DOTALL)

    with open(f_name, 'w', encoding='utf-8') as f:
        f.write(content)
