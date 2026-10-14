"""Tests for scripts/install.py. Installs only into temporary folders."""

import contextlib
import importlib.util
import io
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("install", ROOT / "scripts" / "install.py")
install = importlib.util.module_from_spec(spec)
spec.loader.exec_module(install)


def run(argv, home):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = install.main(argv, home=home)
    return code, buf.getvalue()


class RegistryTests(unittest.TestCase):
    def test_reads_all_skills_and_packs(self):
        skills, packs = install.read_registry()
        self.assertEqual(len(skills), 318)
        self.assertIn("core", packs)
        self.assertIn(("limitation-calculator", "core"), skills)

    def test_every_skill_folder_exists(self):
        skills, _ = install.read_registry()
        for sid, _ in skills:
            self.assertTrue((install.SRC / sid / "SKILL.md").exists(), sid)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.home = pathlib.Path(self.tmp.name) / "home"
        self.addCleanup(self.tmp.cleanup)

    def test_pack_filter_installs_exactly_that_pack(self):
        skills, _ = install.read_registry()
        expected = {s for s, p in skills if p == "core"}
        code, _ = run(["--claude", "--pack", "core"], self.home)
        self.assertEqual(code, 0)
        got = {p.name for p in (self.home / ".claude" / "skills").iterdir()}
        self.assertEqual(got, expected)

    def test_project_targets(self):
        project = pathlib.Path(self.tmp.name) / "proj"
        run(["--project", str(project), "--pack", "core"], self.home)
        for sub in (".claude", ".agents"):
            self.assertTrue((project / sub / "skills" / "limitation-calculator" / "SKILL.md").exists())
            self.assertTrue((project / sub / "skills" / "limitation-calculator" / "scripts" / "date_calc.py").exists())

    def test_antigravity_paths(self):
        run(["--antigravity", "--antigravity-cli", "--pack", "core"], self.home)
        self.assertTrue((self.home / ".gemini" / "config" / "skills" / "limitation-calculator").is_dir())
        self.assertTrue((self.home / ".gemini" / "antigravity-cli" / "skills" / "limitation-calculator").is_dir())

    def test_reinstall_replaces_old_copy(self):
        dest = self.home / ".agents" / "skills"
        stale = dest / "limitation-calculator" / "stale.txt"
        stale.parent.mkdir(parents=True)
        stale.write_text("old", encoding="utf-8")
        run(["--codex", "--pack", "core"], self.home)
        self.assertFalse(stale.exists())

    def test_unknown_pack_rejected(self):
        with self.assertRaises(SystemExit):
            with contextlib.redirect_stderr(io.StringIO()):
                install.main(["--claude", "--pack", "no-such-pack"], home=self.home)
        self.assertFalse((self.home / ".claude").exists())

    def test_no_target_prints_help(self):
        code, out = run(["--pack", "core"], self.home)
        self.assertEqual(code, 2)
        self.assertFalse(self.home.exists())

    def test_list_packs(self):
        code, out = run(["--list-packs"], self.home)
        self.assertEqual(code, 0)
        self.assertIn("criminal-bnss", out)


if __name__ == "__main__":
    unittest.main()
