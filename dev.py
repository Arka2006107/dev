import argparse
with open(out_csv,'w',newline='') as f:
w = csv.writer(f)
w.writerow(['map','planner','path_len','path_cost','nodes_expanded','plan_time_ms'])
w.writerows(rows)
print(f"Experiment results written to {out_csv}")
return rows


# ----------------------------- Report skeleton generator -----------------------------


def write_report_skeleton(fname='report_skeleton.txt'):
text = '''
Autonomous Delivery Agent - Short Report (max 6 pages)


1. Environment model
- Grid representation, cell costs, static obstacles, dynamic obstacles (schedule vs unpredictable)


2. Agent design
- State representation, actions (4-connected), cost model (fuel vs time), replanning policy


3. Heuristics used
- Manhattan*min_cost (admissible), discussion about consistency


4. Implementation details
- Planners implemented (BFS, UCS, A*), local search method (simulated annealing-like shortcutting)


5. Experiments
- Maps: small, medium, large, dynamic
- Table: planner, path cost, nodes expanded, planning time
- Short plots: path cost vs map size (suggest using matplotlib)


6. Analysis and conclusion
- When A* outperforms UCS (heuristic informative), when UCS needed (varying costs), BFS ok for uniform cost maps
- Replanning discussion: horizon knowledge helps avoid collisions; local search useful when unpredictability exists


Appendix: map files, logs, instructions to run.
'''
with open(fname,'w') as f:
f.write(text)
print(f"Report skeleton written to {fname}")


# ----------------------------- Main -----------------------------


def main():
ensure_sample_maps()
parser = argparse.ArgumentParser()
parser.add_argument('--map', default='small', help='map name (small|medium|large|dynamic) or path')
parser.add_argument('--planner', default='astar', help='planner (bfs|ucs|astar)')
parser.add_argument('--show', action='store_true')
parser.add_argument('--log', default=None, help='write simulator log to file')
parser.add_argument('--experiment', default=None, help='run experiments: all')
parser.add_argument('--repeats', type=int, default=3)
args = parser.parse_args()


if args.experiment == 'all':
rows = run_experiments(repeats=args.repeats)
print('Done experiments. See CSV.')
write_report_skeleton()
return


res = run_single(args.map, args.planner, show=args.show, logfile=args.log)
print('Simulation finished. Success=', res['success'])
if args.log:
print('Log written to', args.log)


if __name__ == '__main__':
main()
