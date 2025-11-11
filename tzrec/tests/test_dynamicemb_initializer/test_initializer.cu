#include <cuda_runtime.h>
#include <curand.h>
#include <iostream>

int main(int argc, char* argv[]) {
  int device_id = 0;
  cudaDeviceProp device_prop;
  cudaGetDeviceProperties(&device_prop, device_id);
  std::cout << device_prop.multiProcessorCount << std::endl;
  std::cout << device_prop.warpSize << std::endl;
  std::cout << device_prop.maxThreadsPerMultiProcessor << std::endl;
  std::cout << device_prop.maxThreadsPerBlock << std::endl;
}
