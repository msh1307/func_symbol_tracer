# func_symbol_tracer
EX 1 - syscall trace off) 
```c
0   | - START_TRACE -
1   |   uc_mem_map@plt
2   |     uc_mem_map
3   |       g_tree_new_full@plt
4   |         _dl_runtime_resolve_xsavec
5   |     uc_mem_map
6   |       machine_initialize@plt
7   |         _dl_runtime_resolve_xsavec
8   |     uc_mem_map
9   |       softfloat_init_x86_64
10  |     uc_mem_map
11  |       x86_reg_reset_x86_64
12  |         cpu_x86_update_cr0_x86_64@plt
13  |           cpu_x86_update_cr0_x86_64
14  |             tlb_flush_x86_64@plt
15  |               tlb_flush_x86_64
16  |                 tlb_flush_by_mmuidx_x86_64@plt
17  |                   tlb_flush_by_mmuidx_x86_64
18  |                     gettimeofday@plt
19  |                       gettimeofday
20  |                   tlb_flush_by_mmuidx_x86_64
21  |                     memset@plt
22  |                       __memset_avx2_unaligned_erms
23  |                   tlb_flush_by_mmuidx_x86_64
24  |                     __popcountdi2
25  |                   tlb_flush_by_mmuidx_x86_64
26  |                     __popcountdi2
27  |                   tlb_flush_by_mmuidx_x86_64
28  |           cpu_x86_update_cr0_x86_64
29  |       x86_reg_reset_x86_64
30  |     uc_mem_map
31  |       memory_map_x86_64
32  |         g_malloc@plt
33  |           g_malloc
34  |             malloc@plt
35  |               malloc
36  |       memory_map_x86_64
37  |         memory_region_init_ram_x86_64@plt
38  |           _dl_runtime_resolve_xsavec
39  |       memory_map_x86_64
40  |         memory_region_add_subregion_x86_64@plt
41  |           _dl_runtime_resolve_xsavec
42  |       memory_map_x86_64
43  |             tlb_flush_x86_64@plt
44  |               tlb_flush_x86_64
45  |                 tlb_flush_by_mmuidx_x86_64@plt
46  |                   tlb_flush_by_mmuidx_x86_64
47  |                     gettimeofday@plt
48  |                       gettimeofday
49  |                   tlb_flush_by_mmuidx_x86_64
50  |                     memset@plt
51  |                       __memset_avx2_unaligned_erms
52  |                   tlb_flush_by_mmuidx_x86_64
53  |                     __popcountdi2
54  |                   tlb_flush_by_mmuidx_x86_64
55  |                     __popcountdi2
56  |                   tlb_flush_by_mmuidx_x86_64
57  |       memory_map_x86_64
58  |     uc_mem_map
59  |       mem_map.isra
60  |         g_realloc@plt
61  |           g_realloc
62  |             realloc@plt
63  |               realloc
64  |           g_realloc
65  |       mem_map.isra
66  |         memmove@plt
67  |           __memmove_avx_unaligned_erms
68  |       mem_map.isra
```
EX 2 - syscall trace on)
```c
0   | - START_TRACE -
1   |   go
2   |     malloc@plt
3   |       malloc
4   |   go
5   |     go1
6   |       read@plt
7   |         read
8   |     go1
9   |   go
10  |     main
```
