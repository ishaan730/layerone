"""Regenerate every page. Run: python3 tools/build/build_all.py"""
import runpy, os
here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)
for name in ["home", "pages", "pricing", "contact", "cs_tokens", "cs_governance", "cs_patterns", "article"]:
    runpy.run_path(os.path.join(here, name + ".py"), run_name="__main__")
