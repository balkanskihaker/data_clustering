<h2>
  Mouse kidney transcriptomics problem
</h2><br>
<p>
  Need to cluster cells of mouse kindey tissue into n clusters.
</p>
<p>
  Dataset contains following columns: <b>geneID, x, y, MIDCount, ExonCount, CellID</b> and contains more than 8 million rows
</p>
<p>
  I done some data preprocessing, like changing dtype to reduce memory footpring, creating algorithm to reduce number of rows, loging etc...
</p>
<p>
  I tried different number of cluster, from 14 to 64, and range from 14 to 20 gave me best results.<br>
  Using Silhouette scoring and looking for score close to 0.<br>
  Kmeans on <b>unloged_reduced_pca_095</b> data <b>with n_cluster=18</b> gave me the best results, 0.0128.<br>
  <br>
  'unloged_reduced_pca_095' means that data is not loged, it's reduced with my algorithm and it's passed trough PCA with n_components=0.95.
</p>
<br>
<p>
  I can not share dataset due it's confidentiality.
</p>
