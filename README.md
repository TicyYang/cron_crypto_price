主機環境為Ubuntu 22.04


Dockerfile設置包含：
基礎image為python:3.10-alpine
時區設為台北




自動排程透過以下指令設置：
crontab -e
*/1 * * * * docker start crypto_ctr