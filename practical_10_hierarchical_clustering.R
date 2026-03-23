# Practical - 10
# Aim: To implement hierarchical clustering using R

# Step 1: Create data
data <- data.frame(
  x = c(2, 3, 8, 7, 3),
  y = c(2, 7, 2, 8, 3)
)
rownames(data) <- c("A", "B", "C", "D", "E")

# Step 2: Distance matrix
d <- dist(data, method = "euclidean")

# Step 3: Hierarchical clustering
hc <- hclust(d, method = "single")

# Step 4: Plot dendrogram
plot(hc, main = "Hierarchical Clustering (Single Link)")

# Step 5: Form clusters
clusters <- cutree(hc, k = 2)
print(clusters)
