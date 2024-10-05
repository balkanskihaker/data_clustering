<h2>Mouse kidney transcriptomics problem</h2>
<br>
<p>Need to construct image of tissue and to cluster cells into x clusters.</p>
<p>Dataset contains following columns: <b>geneID, x, y, MIDCount, ExonCount, CellID</b><br>and contains more than 8 million rows. All values are int64 by default.</p>
<br>
<p>I'm working on two different machines so that's why are there two codes, <b>cupy.ipynb</b> and <b>numpy.ipynb</b>,
difference is that I'm using nvidia gpu for heavy workload in one and in the other I don't, respectively.</p>
<p>Before starting preprocessing data I'm changing data type from int64 to uint16 and uint8 to reduce memory footprint</p>
<p>First step is to extract unique cells and genes for creation of <b>cell-gene</b> matrix that will be filled with <b>MIDCount.</b></p>
<p>Next problem is to find the fastest way to fill that matrix with <b>MIDCount</b> because of it's dimensions 62725 by 20753, or more than 1.3 billion of values to be filled.
The fastest way I found is by using <b>pandas.Factorize</b> creates numerical values that maps to actual values.</p>
<p>Now that matrix needs to be loged to minimize distance between values, before loging I'm upgrading data type to float32 to get better precision.
Problem is that I can not load 1.3 billion float32 values in gpu at once, limited memory, so I splited loging into two parts.
In numpy code that's not a problem because there's enough of ram, and virtual memory if needed, but I still left the code to log in two parts.</p>
<p>Last step of solving the problem is to run different cluster functions with different number of clusters. Using clustering methods from <b>CuML</b> is sadly out of question because of limited resources, 
but scikit-learn methods, cpu intensive, are there.</p>
<p>Only thing left to do is to visualize that tissue with clustered cells.</p>
<p><b>IMPORTANT<br>
I can not share data set or any image due to confidentiality.</b><p>
