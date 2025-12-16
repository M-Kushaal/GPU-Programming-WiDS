# CS61C FA20 — Lecture 39: GPU Guest Lecture (James Percy, Apple)

## Learning Goals

By the end of this lecture, you should be able to:

* Explain the architectural differences between CPUs and GPUs
* Understand why GPUs prioritize throughput over latency
* Identify key GPU pipeline stages
* Understand SIMD/SIMT execution models
* Recognize workloads that benefit from GPU acceleration

---

## What Is a GPU?

* CPUs have a small number of complex cores optimized for low-latency, serial tasks
* GPUs have hundreds to thousands of simpler cores optimized for parallel throughput
* GPUs excel at data-parallel workloads such as graphics and matrix operations

**Key Idea**: GPUs trade complex control logic for massive parallel execution.

---

## GPU Architecture Overview

### CPUs
* Few powerful cores
* Large caches and branch prediction
* Optimized for sequential execution

### GPUs
* Many lightweight cores
* High memory bandwidth
* Designed for thousands of concurrent threads

---

## Performance Model

* Throughput-oriented, not latency-oriented
* SIMD / SIMT execution
* Thread-level parallelism hides memory latency
* High utilization is critical for performance

---

## GPU Rendering Pipeline

1. Vertex Processing  
2. Primitive Assembly  
3. Rasterization  
4. Fragment (Pixel) Processing  
5. Output Merging

Modern GPUs use **unified shader cores** across stages.

---

## Shader Programming

* Programmable shaders replaced fixed-function pipelines
* Common shader languages:
  * Metal
  * CUDA
  * GLSL / HLSL
* Same program runs across many vertices or pixels in parallel

---

## Parallel Execution Model

* Threads execute in groups (warps / threadgroups)
* All threads in a group execute the same instruction
* Hardware schedules other warps during stalls

---

## Texture Mapping

* Textures are images mapped onto surfaces
* Texture units handle sampling and filtering
* Enables detailed and realistic rendering

---

## CPU vs GPU Demo

* Scalar multiply example
* CPU faster for small data sizes (lower overhead)
* GPU faster for large data sizes due to parallelism
* Demonstrates importance of problem size

---

## Key Takeaways

* Maximize parallelism
* Design for throughput
* Use GPU-friendly memory access patterns
* GPUs power graphics, ML, photography, autonomy, and crypto

---

## Notes

Lecture slides and transcript are not publicly distributed.
Recording available to enrolled students.

