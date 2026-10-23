"""Regenerate every page except the hand-written article. Run: python3 tools/build/build_all.py"""
import runpy, os
here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)
for name in ["home", "pages", "cs_tokens", "cs_governance", "cs_patterns"]:
    runpy.run_path(os.path.join(here, name + ".py"), run_name="__main__")
