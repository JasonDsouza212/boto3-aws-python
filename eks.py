import boto3

client= boto3.client("eks")
clusters =client.list_clusters()['clusters']

for cluster in clusters:
    response =client.describe_cluster(
        name=cluster
    )
    cluster_status= response['cluster']['status']
    cluster_endpoint = response['cluster']['endpoint']
    print(f"Cluster {cluster} status is {cluster_status}")
    cluster_version = response['cluster']['version']
    print(f"Cluster endpoint: {cluster_endpoint}")
    print(f" The version is {cluster_version}")

