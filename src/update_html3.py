import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

chrome_css = r'''
        .chrome-text {
            background: linear-gradient(to bottom right, #f8fafc 0%, #94a3b8 40%, #ffffff 50%, #64748b 60%, #cbd5e1 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-shadow: 0px 1px 3px rgba(0,0,0,0.8);
        }

        body, p, h1, h2, a, div, span, .disclaimer, .bio-content, .quote {
            color: transparent;
        }

        /* Override links */
        .menu-item, .btn-enter, .btn-back {
            background: linear-gradient(to bottom right, #e2e8f0 0%, #9ca3af 45%, #ffffff 50%, #475569 55%, #cbd5e1 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-shadow: 0px 1px 2px rgba(0,0,0,0.8);
        }
        
        .menu-item:hover, .btn-enter:hover, .btn-back:hover {
            background: linear-gradient(to bottom right, #ffffff 0%, #cbd5e1 45%, #64748b 50%, #ffffff 55%, #e2e8f0 100%);
            -webkit-background-clip: text;
            background-clip: text;
            text-shadow: 0px 0px 10px rgba(255,255,255,0.4);
            color: transparent;
        }
'''

for f_name in html_files:
    with open(f_name, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the broken block
    broken_block = re.search(r'\.chrome-text\s*\{\s*text-shadow:.*?\col\s*\}\s*', content, re.DOTALL)
    
    # Just replace from .chrome-text to the end of style
    content = re.sub(r'\.chrome-text\s*\{.*?</style>', chrome_css + '\n    </style>', content, flags=re.DOTALL)
    
    # Also fix double class attributes like: class="chrome-text" class="contact-prompt"
    content = re.sub(r'class="chrome-text" class="([^"]+)"', r'class="\1 chrome-text"', content)

    # Some elements might just have text-color transparent but not be chrome text.
    # The chrome_css applies to everything, but wait...
    # If `body, p, a, div` have `color: transparent`, and they don't have `.chrome-text`, they become invisible!
    # Let me fix my CSS!
    
    better_chrome_css = r'''
        body, p, h1, h2, a, div, span, .disclaimer, .bio-content, .quote {
            /* Remove global transparent color since we explicitly add chrome-text */
            color: #cbd5e1;
        }

        .chrome-text, h1, h2, p, .subtitle, .disclaimer, .phone {
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
    content = re.sub(r'\.chrome-text\s*\{.*?</style>', better_chrome_css + '\n    </style>', content, flags=re.DOTALL)

    with open(f_name, 'w', encoding='utf-8') as f:
        f.write(content)
