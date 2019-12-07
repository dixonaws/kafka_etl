#!/bin/bash
aws kafka describe-cluster --region eu-central-1 --cluster-arn $kafka_cluster_arn |jq '.ClusterInfo.ZookeeperConnectString'

export ZookeeperConnectString=`aws kafka describe-cluster --region eu-central-1 --cluster-arn $kafka_cluster_arn |jq '.ClusterInfo.ZookeeperConnectString'`

