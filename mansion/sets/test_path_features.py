"""Boundary and preservation checks for the shared path plan.
Codex (OpenAI), 2026-10-23. Run in mansion/sets: python3 -m unittest test_path_features.py
"""
import copy, re, unittest
from fractions import Fraction
import build_sets, path_features, shares

class PlanChecks(unittest.TestCase):
    def test_transition_is_data_not_a_hidden_path_rule(self):
        data=path_features.load()
        self.assertEqual(path_features.mode_at("number-form",1,["3-c"],data),"decimals")
        self.assertEqual(path_features.mode_at("number-form",2,["1-c"],data),"decimals")
        self.assertEqual(path_features.mode_at("number-form",2,["2-a"],data),"decimals")
        self.assertEqual(path_features.mode_at("number-form",2,["6-a"],data),"fractions")
        self.assertEqual(path_features.mode_at("number-form",3,[],data),"fractions")
        path_features.feature("number-form",data)["paths"]["2"]["then"]["starts_at"]="2-c"
        sample=[("p","(2-a) 1.6 N"),("p","(2-c) 0.75 crank"),("p","0.375 crank")]
        got=shares.apply(sample,path=2,plan=data)
        self.assertIn("1.6 N",got[0][1])
        self.assertIn("3/4 crank",got[1][1])
        self.assertIn("3/8 crank",got[2][1])
    def test_spool_force_and_torque_are_preserved(self):
        f=Fraction
        self.assertEqual(f(8,5),6-f(22,5))
        self.assertEqual(f(22,5)*f(1,5)-6*f(3,25),f(1,25)*4)
        sample=[("p","(3-c) The center needs 1.6 N; friction is 4.4 N."),
                ("eq","(m + I/R²)a = F(1 − r/R)"),
                ("p","2.4 N at the axle.")]
        out=shares.apply(sample,path=3)
        self.assertIn("8/5 N",out[0][1]); self.assertIn("22/5 N",out[0][1])
        self.assertEqual(out[2][1],"12/5 N at the axle.")
    def test_rounding_is_not_promoted_to_exactness(self):
        self.assertEqual("√6, about 2.4 m/s",shares.convert("√6, about 2.4 m/s",mode="fractions",part="4-c"))
        self.assertEqual("q₀ ≈ 0.52 C",shares.convert("q₀ ≈ 0.52 C",mode="fractions",part="13-a"))
        self.assertIn("3/8",shares.convert("χ = 0.38 crank",mode="fractions",part="2-c"))
        self.assertEqual("χ = 0.375 crank",shares.convert("χ = 0.38 crank",mode="decimals",part="2-c"))
        self.assertEqual(shares.convert("6.0 N",mode="decimals"),"6 N")
        self.assertEqual("pile up every 1.8 s",shares.convert("pile up every 1.8 s",part="1-γ"))
        self.assertEqual("0.041 m/s",shares.convert("0.041 m/s",part="9-c"))
    def test_units_and_the_built_roundings(self):
        self.assertEqual("40 g m²; 500 g m²; 1 kg m²; 40 g m²/s; 5 mm",shares.convert("0.040 kg m²; 0.50 kg m²; 1000 g m²; 0.04 kg m²/s; 0.005 m"))
        self.assertEqual("1/3 kg m²",shares.convert("1/3 kg m²"))
        for k in (1,2,3,4):
            text="\n".join(s for _,s in build_sets.build(k))
            self.assertIsNone(re.search(r"(?:about|≈)\s+\(?\d+/\d+",text))
            self.assertNotIn("63/10 strokes",text)
            self.assertIn("3/5",text)
            self.assertGreater(path_features.observe(build_sets.build(k),k)["decimal_count"],0)
    def test_a_source_edit_cannot_be_silently_overwritten(self):
        with self.assertRaises(AssertionError):
            build_sets.checked_solution([("p","(a-4) a later correction")],"(a-4)","(a-4) the old source","replacement")
    def test_poetry_states_are_editorial_not_automatic_proof(self):
        data=path_features.load()
        for feature in data["features"]:
            if feature["kind"] in {"poetry","narrative"}:
                self.assertEqual(feature["implementation"],"editorial")
        self.assertEqual(path_features.feature("rhythmic-structure",data)["status"],"planned")
        self.assertEqual(path_features.feature("finale",data)["status"],"protected")
    def test_export_has_one_four_path_plan(self):
        data=path_features.load()
        self.assertEqual(len({f["id"] for f in data["features"]}),len(data["features"]))
        self.assertTrue(all(set(f["paths"])=={"1","2","3","4"} for f in data["features"]))
        panel=path_features.panel(data)
        self.assertIn('id="features-export"',panel)
        self.assertIn('id="features-reset"',panel)
        self.assertIn('Nothing here writes to Google Docs',panel)

if __name__=="__main__":
    unittest.main()
