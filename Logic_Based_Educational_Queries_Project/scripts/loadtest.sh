#!/bin/bash

URL="https://a56e-136-110-8-164.ngrok-free.app/predict"
NUM_REQUESTS=50

RED='\033[0;31m'
NC='\033[0m'

read -r -d '' PAYLOAD << 'EOF'
{
  "options": [],
  "premises": [
    "If a researcher completed ethics training and has lab access, then that researcher can handle participant data.",
    "If a researcher can handle participant data and has supervisor approval, then that researcher may join Study Alpha.",
    "Every researcher who may join Study Alpha is listed as an active contributor.",
    "Asha completed ethics training.",
    "Asha has lab access.",
    "Asha has supervisor approval.",
    "Study Alpha has 12 enrolled participants.",
    "No premise states whether Asha has budget approval.",
    "If a researcher is listed as an active contributor, they must submit a monthly progress report.",
    "All monthly progress reports are archived in the central institutional repository.",
    "Dr. Khan is the head supervisor of Study Alpha and reviews all member applications.",
    "If a researcher fails to submit a monthly progress report, their lab access will be temporarily suspended.",
    "Ethics training certificates are valid for a duration of exactly two calendar years.",
    "Funding for Study Alpha is provided by the National Science Foundation grant number 405-A.",
    "Any active contributor who handles participant data must undergo an additional background check.",
    "Asha has already cleared the institutional background check requirement.",
    "The institutional repository is managed by the university library department."
  ],
  "query": "Which researcher may join Study Alpha and what are their data handling obligations?",
  "query_id": "extended_type1_text",
  "type": "type1"
}
EOF

echo "Dang chay load test, hien thi Response va bat loi (Raise Error)..."

for ((i=1; i<=NUM_REQUESTS; i++))
do
   {
       RESPONSE=$(curl -s --fail-with-body -X POST "$URL" \
            -H "Content-Type: application/json" \
            -d "$PAYLOAD")

       EXIT_CODE=$?

       if [ $EXIT_CODE -ne 0 ]; then
           echo -e "${RED}\n!!! [ERROR - Request #$i] !!!"
           echo -e "Loi cURL / Server ma: $EXIT_CODE"
           echo -e "Chi tiet phan hoi loi tu server (neu co):"
           echo -e "$RESPONSE${NC}"
           echo -e "${RED}------------------------${NC}"
       else
           echo -e "\n=== [Request #$i] ==="
           echo "$RESPONSE"
           echo -e "------------------------"
       fi
   } &

   if [ $((i % 10)) -eq 0 ]; then
       sleep 0.1
   fi
done

wait
echo -e "\nDa nhan xong toan bo response."
