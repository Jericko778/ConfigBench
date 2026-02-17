ConfigBench is a tool for automating the testing of performance for the configurations of static analysis tools. Might require tweaking the code to work for different terminals.

Made in the UTD Clark research program.

ConfigBench: Automated Performance Testing for Static Analysis Tools to Evaluate Performance Trade-Offs

John John Veslin, Austin Mordahl, Shiyi Wei

Erik Jonsson School of Engineering and Computer Science, The University of Texas at Dallas

Abstract

Static analysis tools analyze programs without executing them. They are helpful as they expedite the discovery of software bugs and vulnerabilities, reducing the effort required to check the code. However, no single static analysis can effectively handle all types of target programs, so, popular static analysis tools have various configuration options that alter their performance and behavior, allowing the user to fine-tune the analysis to their specific needs. However, the performance trade-offs between configuration options are not fully understood as manually testing performance is tedious due to the tools' large configuration spaces. While determining the time complexity of the configuration options’ algorithms is possible, it is difficult as static analysis often runs multiple different algorithms, sometimes concurrently, necessitating an empirical approach. This lack of knowledge regarding configuration performance trade-offs can lead users to suboptimal tool usage and wasted time. To address this, we designed a tool to automate performance testing of various configurations for static analysis tools. We integrated the static taint analysis tool, FlowDroid, to perform single configuration option tests, showing that 13 of the 47 individual configuration option settings tested had a statistically significant impact on the performance. Our evaluation reveals some unexpected results, such as the “fast” callback analyzer setting running slower than the default. We plan to expand our work by integrating and testing additional static analysis tools like WALA and SootUp. We also aim to aid the developers of static analysis tools by reporting our findings, especially unexpected ones.


<img width="870" height="590" alt="image" src="https://github.com/user-attachments/assets/e639849c-8a0f-4208-beaa-f2c0d1a18389" />
