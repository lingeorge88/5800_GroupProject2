from __future__ import annotations
import random, time, tracemalloc, csv, pathlib
from typing import List
import matplotlib.pyplot as plt
import pandas as pd
from maxSkylineSol import Solution

# ─────────────────────────────── benchmark ──────────────────────────────
def benchmark(func: Callable, label: str,
              sizes: list[int], runs: int = 3) -> pd.DataFrame:
    rec = []
    for n in sizes:
        grid = [[random.randint(0, 100) for _ in range(n)] for _ in range(n)]
        tracemalloc.start()
        t_total = 0.0
        for _ in range(runs):
            t0 = time.perf_counter()
            func(grid)
            t_total += time.perf_counter() - t0
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        rec.append(dict(
            n=n,
            runtime_ms=(t_total / runs) * 1_000,
            peak_kib=peak / 1024,
            algo=label,
        ))
    return pd.DataFrame(rec)

# ───────────────────────── plot ────────────────────────────────────
def plot_curves(df_all: pd.DataFrame, out_dir: pathlib.Path):
    colors = {"solution1": "C0", "solution2": "C1"}
    
    # Runtime
    plt.figure()
    for name, d in df_all.groupby("algo"):
        plt.plot(d["n"], d["runtime_ms"], "o-", color=colors[name], label=name)
    plt.title("Runtime (ms)"); plt.xlabel("n"); plt.ylabel("ms")
    plt.legend(); plt.grid(True); plt.tight_layout()
    plt.savefig(out_dir / "runtime.png", dpi=150)

    # Memory
    plt.figure()
    for name, d in df_all.groupby("algo"):
        plt.plot(d["n"], d["peak_kib"], "s-", color=colors[name], label=name)
    plt.title("Peak memory (KiB)"); plt.xlabel("n"); plt.ylabel("KiB")
    plt.legend(); plt.grid(True); plt.tight_layout()
    plt.savefig(out_dir / "memory.png", dpi=150)
    plt.show()

def profile(func, grid: List[List[int]], runs=3):
    tracemalloc.start()
    t_total = 0
    for _ in range(runs):
        t0 = time.perf_counter()
        func([row[:] for row in grid])   
        t_total += time.perf_counter() - t0
    cur, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return (t_total/runs*1000, peak/1024)  



def main():
    sol = Solution()
    sizes = [2, 10, 20, 40, 80, 120, 160, 200, 500, 800, 1000]
    solution1 = benchmark(sol.maxIncreaseKeepingSkyline1, "solution1", sizes, runs=5)
    solution2 = benchmark(sol.maxIncreaseKeepingSkyline2, "solution2", sizes, runs=5)

    df_all = pd.concat([solution1, solution2]).sort_values(["algo", "n"])
    print(df_all)

    out_dir = pathlib.Path("MaxSkyline_Runtime_Compare")
    out_dir.mkdir(exist_ok=True)
    #df_all.to_csv(out_dir / "runtime_space_compare.csv", index=False)
    plot_curves(df_all, out_dir)
    print("Charts saved to:", out_dir.resolve())


    greedy = sol.maxIncreaseKeepingSkyline2
    brute  = sol.maxIncreaseKeepingSkyline3
    for n in (1,2):
        #if n > 2, the runtime will be a super large number. from n in 1 and 2, we already see the huge runtime different 
        # showing greedy is a better strategies.
        grid = [[random.randint(0, 5) for _ in range(n)] for _ in range(n)]
        t_g, m_g = profile(greedy, grid)
        t_b, m_b = profile(brute,  grid, runs=1)   
        print(f"n={n}: greedy {t_g:.3f} ms | {m_g:.1f} KiB   "
            f">> brute {t_b:.3f} ms | {m_b:.1f} KiB")


if __name__ == "__main__":
    main()