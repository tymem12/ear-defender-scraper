# 🕸️ EarDefender – Scraper

**Automated Web Scraping & Audio Retrieval Module**

## 🚀 Overview

The **Scraper** Module is responsible for collecting audio content from websites and online platforms.

It automates:
- Navigating webpages (including dynamically loaded content)
- Following subpage links
- Extracting audio/video resources
- Downloading files using tools like **Selenium** and **yt-dlp**

Thanks to automation and optimized crawling logic, the scraper removes the need for manual uploads and enables efficient large-scale dataset collection. It plays a crucial role in the system’s overall performance and scalability.

## ⚙️ Features

- Automated browsing with **Selenium WebDriver**
- High-reliability media downloading via **yt-dlp**
- Support for dynamic pages, scrolling, and interactive content
- Extraction from both main pages & nested subpages
- Containerized service ready to interact with the Connector module
- Designed for scalability and multi-source scraping

## 🐳 Local Run (Docker)
1. **Build Docker image**
   
`docker build -t scraper-app .`

2. **Run container**

Expose port 8000 and increase shared memory for Selenium:

`docker run -p 8000:8000 --shm-size=2g scraper-app`


***Note**: The increased `--shm-size` prevents browser crashes during complex Selenium sessions.*
