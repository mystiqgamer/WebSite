"""
KTU ScholarOS - Automated Test Suite (B.Tech 2024 Scheme - Revised Regulations)
Validates S1-S4 course syllabi, 120 Activity Points Three-Group Rule, and CIE calculations.
"""

import sys
import unittest
from app import app

class TestKTUScholarOS2024(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health_and_overview(self):
        res = self.client.get("/api/health")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["status"], "healthy")
        self.assertIn("120 Activity Points", data["regulations"])

        res_ov = self.client.get("/api/overview")
        self.assertEqual(res_ov.status_code, 200)
        ov = res_ov.get_json()
        self.assertEqual(ov["stats"]["activity_points_required"], 120)
        self.assertEqual(ov["stats"]["min_points_per_group"], 40)
        self.assertEqual(ov["stats"]["activity_groups"], 3)
        self.assertGreaterEqual(ov["stats"]["ktu_courses"], 6)

    def test_cie_calculator(self):
        res = self.client.post("/api/calculator/cie", json={
            "series1": 35.0,
            "series2": 40.0,
            "assignment": 14.0,
            "attendance_pct": 92.0
        })
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["cie_total"], 42.8) # (37.5/50)*25 + 14 + 10 = 18.75 + 14 + 10 = 42.75 -> 42.8
        self.assertEqual(data["supply_risk"], "LOW")

    def test_s1_to_s4_courses(self):
        res = self.client.get("/api/courses")
        self.assertEqual(res.status_code, 200)
        courses = res.get_json()["courses"]
        course_codes = [c["code"] for c in courses]
        self.assertIn("MAT 101", course_codes)
        self.assertIn("EST 102", course_codes)
        self.assertIn("CST 201", course_codes)
        self.assertIn("CST 202", course_codes)
        self.assertIn("CST 204", course_codes)
        self.assertIn("CST 206", course_codes)

    def test_activity_points_three_group_rule(self):
        # 1. Test Deficit: Only Group 3 has points
        res_deficit = self.client.post("/api/activity_points/audit", json={
            "user_activities": [
                {"group_id": "group-3", "name": "NPTEL Course", "points": 50}
            ]
        })
        self.assertEqual(res_deficit.status_code, 200)
        d_data = res_deficit.get_json()
        self.assertFalse(d_data["is_degree_eligible"])
        self.assertFalse(d_data["three_group_compliance"])
        self.assertIn("Failed Three-Group Rule", d_data["verdict"])

        # 2. Test Success: All 3 groups have at least 40 points and total >= 120
        res_success = self.client.post("/api/activity_points/audit", json={
            "user_activities": [
                {"group_id": "group-1", "name": "NSS", "points": 45},
                {"group_id": "group-2", "name": "Sports", "points": 40},
                {"group_id": "group-3", "name": "NPTEL + Hackathon", "points": 50}
            ]
        })
        self.assertEqual(res_success.status_code, 200)
        s_data = res_success.get_json()
        self.assertTrue(s_data["is_degree_eligible"])
        self.assertTrue(s_data["three_group_compliance"])
        self.assertGreaterEqual(s_data["total_verified_points"], 120)

    def test_ktu_simulations(self):
        res_cpu = self.client.post("/api/simulations/cpu_scheduling", json={
            "processes": [{"name": "P1", "arrival": 0, "burst": 4}],
            "quantum": 2
        })
        self.assertEqual(res_cpu.status_code, 200)

        res_kmap = self.client.post("/api/simulations/kmap", json={"minterms": [0, 1, 2, 3]})
        self.assertEqual(res_kmap.status_code, 200)

        res_bst = self.client.post("/api/simulations/bst", json={"elements": [10, 5, 15]})
        self.assertEqual(res_bst.status_code, 200)

if __name__ == "__main__":
    unittest.main()
