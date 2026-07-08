import importlib.util
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_example_solution(name):
    path = ROOT / name
    source = path.read_text()
    marker = '# Example Solution'
    start = source.index(marker)
    match = re.search(r'"""(.*?)"""', source[start:], re.S)
    if not match:
        raise AssertionError(f'Example solution not found in {name}')
    code = match.group(1)
    namespace = {}
    module = importlib.util.module_from_spec(importlib.util.spec_from_file_location(name[:-3], path))
    spec = importlib.util.spec_from_file_location(name[:-3], path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    namespace['data'] = module.data
    exec(code, namespace)
    return namespace['solve']


class ListsExerciseTests(unittest.TestCase):
    def test_001_interface_inventory_filter(self):
        solve = load_example_solution('001_interface_inventory_filter.py')
        self.assertEqual(solve(solve.__globals__['data']), [
            {'name': 'Gi0/1', 'description': 'uplink', 'speed': '10G'},
            {'name': 'Gi0/3', 'description': 'storage', 'speed': '25G'},
        ])

    def test_002_vlan_command_builder(self):
        solve = load_example_solution('002_vlan_command_builder.py')
        self.assertEqual(solve(solve.__globals__['data']), [
            'vlan 0010 name DATA',
            'vlan 0020 name VOICE',
            'vlan 0030 name MGMT',
            'vlan 0100 name SERVERS',
        ])

    def test_003_maintenance_queue_update(self):
        solve = load_example_solution('003_maintenance_queue_update.py')
        self.assertEqual(solve(solve.__globals__['data']), ['emergency-core', 'backup-core', 'audit-fw', 'post-check'])

    def test_004_route_metric_top_three(self):
        solve = load_example_solution('004_route_metric_top_three.py')
        self.assertEqual(solve(solve.__globals__['data']), [
            {'prefix': '10.0.2.0/24', 'next_hop': 'wan3', 'metric': 5, 'active': True},
            {'prefix': '10.0.0.0/24', 'next_hop': 'wan1', 'metric': 10, 'active': True},
            {'prefix': '10.0.1.0/24', 'next_hop': 'wan2', 'metric': 20, 'active': True},
        ])

    def test_005_neighbor_row_report(self):
        solve = load_example_solution('005_neighbor_row_report.py')
        self.assertEqual(solve(solve.__globals__['data']), [
            'r1 Gi0/1 -> sw1 Gi0/24',
            'r2 Gi0/2 -> sw2 Gi0/24',
        ])

    def test_006_flatten_command_batches(self):
        solve = load_example_solution('006_flatten_command_batches.py')
        self.assertEqual(solve(solve.__globals__['data']), [
            'terminal length 0',
            'show clock',
            'show ip interface brief',
            'show version',
            'show inventory',
        ])

    def test_007_sliding_error_windows(self):
        solve = load_example_solution('007_sliding_error_windows.py')
        self.assertEqual(solve(solve.__globals__['data']), [
            {'start': 0, 'end': 2, 'errors': 3},
            {'start': 1, 'end': 3, 'errors': 4},
            {'start': 2, 'end': 4, 'errors': 5},
            {'start': 3, 'end': 5, 'errors': 6},
        ])

    def test_008_deduplicate_devices_order(self):
        solve = load_example_solution('008_deduplicate_devices_order.py')
        self.assertEqual(solve(solve.__globals__['data']), ['r1', 'sw1', 'fw1', 'r2'])

    def test_009_zip_interface_descriptions(self):
        solve = load_example_solution('009_zip_interface_descriptions.py')
        self.assertEqual(solve(solve.__globals__['data']), [
            {'interface': 'Gi0/1', 'description': 'uplink', 'role': 'core'},
            {'interface': 'Gi0/2', 'description': 'server', 'role': 'access'},
            {'interface': 'Gi0/3', 'description': 'spare', 'role': 'edge'},
        ])

    def test_010_change_plan_stages(self):
        solve = load_example_solution('010_change_plan_stages.py')
        self.assertEqual(solve(solve.__globals__['data']), ['validate', 'verify', 'deploy', 'rollback'])


if __name__ == '__main__':
    unittest.main()
