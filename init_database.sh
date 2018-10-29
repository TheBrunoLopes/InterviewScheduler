#!/usr/bin/env bash
interview_scheduler_service=interviewscheduler_InterviewScheduler-service_1
docker exec -it ${interview_scheduler_service} python3 init_mongo.py
