<template>
  <div class="map-container-wrapper">
    <div class="map-header">
      <h2 class="map-title">📍 {{ todayLabel }} 실시간 혼잡도 지도</h2>
      <div class="map-legend">
        <span class="legend-item"><span class="dot green"></span>여유</span>
        <span class="legend-item"><span class="dot yellow"></span>보통</span>
        <span class="legend-item"><span class="dot red"></span>혼잡</span>
      </div>
    </div>
    <div id="map" class="festival-map"></div>
  </div>
</template>

<script setup>
import { getEffectiveTodayNumber, getEffectiveToday } from '@/config/demoDate'
import { onMounted, onUnmounted } from 'vue'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'

// 73개 상세 데이터 원본 전체가 완벽하게 보존된 JSON 로드
import festivalData from '@/assets/data/서울_축제공연행사.json'

let map = null
const markersMap = new Map()
const today = getEffectiveToday()
const todayLabel = `${today.getFullYear()}년 ${today.getMonth() + 1}월 ${today.getDate()}일`

// 🎨 1. 상태에 따른 동적 SVG 물방울 마커 생성기
function createCongestionIcon(status) {
  let color = '#10b981' // 여유: 초록
  if (status === '보통') color = '#f59e0b' // 보통: 노랑
  if (status === '혼잡') color = '#ef4444' // 혼잡: 빨강

  const svgHtml = `
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="${color}" width="32" height="32" style="filter: drop-shadow(0px 3px 5px rgba(0,0,0,0.3));">
      <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/>
    </svg>
  `
  return L.divIcon({
    html: svgHtml,
    className: 'custom-congestion-icon',
    iconSize: [32, 32],
    iconAnchor: [16, 32],
    popupAnchor: [0, -32]
  })
}

// 💡 [가중치 수치 연산] (여유*10 + 보통*50 + 혼잡*100) / 전체 개수
function calculateCongestionFromComments(comments) {
  if (!comments || comments.length === 0) return { status: '여유', score: 10 }

  let greenCount = 0, yellowCount = 0, redCount = 0
  comments.forEach(comment => {
    if (comment.tag === '혼잡') redCount++
    else if (comment.tag === '보통') yellowCount++
    else greenCount++
  })

  const total = greenCount + yellowCount + redCount
  const totalScore = (greenCount * 10) + (yellowCount * 50) + (redCount * 100)
  const averageScore = Math.round(totalScore / total)

  let status = '여유'
  if (averageScore >= 75) status = '혼잡'
  else if (averageScore >= 35) status = '보통'

  return { status, score: averageScore }
}

// 💡 [실시간 제보 처리 전역 함수]
window.reportCongestion = (contentId, selectedStatus) => {
  const markerInfo = markersMap.get(contentId)
  if (markerInfo) {
    if (!markerInfo.item.communityComments) {
      markerInfo.item.communityComments = []
    }
    
    markerInfo.item.communityComments.push({
      author: "실시간_제보자",
      content: `방금 들어온 소식! 현재 현장은 [${selectedStatus}] 상태입니다.`,
      tag: selectedStatus
    })

    const { status: newCalculatedStatus, score } = calculateCongestionFromComments(markerInfo.item.communityComments)

    markerInfo.marker.setIcon(createCongestionIcon(newCalculatedStatus))

    const newPopupContent = generatePopupContent(markerInfo.item, newCalculatedStatus, score)
    markerInfo.marker.setPopupContent(newPopupContent)
    markerInfo.marker.openPopup()

    alert(`🎉 제보 반영 성공! 가중치 지수가 ${score}점이 되어 마커가 [${newCalculatedStatus}]으로 변경되었습니다!`)
  }
}

// 💬 팝업 말풍선 레이아웃 구성기
function generatePopupContent(festival, calculatedStatus, score) {
  let badgeColor = '#10b981'
  if (calculatedStatus === '보통') badgeColor = '#f59e0b'
  if (calculatedStatus === '혼잡') badgeColor = '#ef4444'

  let commentsHtml = ''
  if (festival.communityComments && festival.communityComments.length > 0) {
    commentsHtml = festival.communityComments.slice(-3).reverse().map(c => `
      <div style="margin-bottom: 6px; background: #f8fafc; padding: 6px 8px; border-radius: 6px; border-left: 3px solid ${badgeColor};">
        <span style="font-size: 10px; color: #64748b; font-weight: bold;">@${c.author}</span>
        <p style="margin: 2px 0 0 0; font-size: 11px; color: #334155; line-height: 1.3;">"${c.content}"</p>
      </div>
    `).join('')
  } else {
    commentsHtml = `<div style="text-align: center; color: #94a3b8; font-size: 11px; padding: 10px 0;">아직 실시간 커뮤니티 제보가 없습니다.</div>`
  }

  return `
    <div style="font-family: sans-serif; padding: 4px; width: 250px;">
      <strong style="font-size: 14px; color: #1e293b; display: block; margin-bottom: 4px;">🎉 ${festival.title}</strong>
      
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
        <span style="display: inline-block; background-color: ${badgeColor}; color: white; font-size: 11px; padding: 2px 6px; border-radius: 4px; font-weight: bold;">
          ${calculatedStatus} (${score}점)
        </span>
        <span style="font-size: 11px; color: #64748b; font-weight: bold;">제보 ${festival.communityComments ? festival.communityComments.length : 0}건</span>
      </div>

      <div style="width: 100%; height: 6px; background-color: #e2e8f0; border-radius: 3px; overflow: hidden; margin-bottom: 10px;">
        <div style="width: ${score}%; height: 100%; background-color: ${badgeColor}; transition: width 0.5s ease;"></div>
      </div>

      <p style="margin: 0 0 10px 0; font-size: 11px; color: #64748b; line-height: 1.4;">
        <strong>장소:</strong> ${festival.addr1 || '서울 일대'}
      </p>

      <div style="margin-top: 5px; border-top: 1px dashed #cbd5e1; padding-top: 8px;">
        <span style="font-size: 11px; color: #1e293b; font-weight: bold; display: block; margin-bottom: 6px;">💬 실시간 게시판 후기</span>
        <div style="max-height: 120px; overflow-y: auto;">
          ${commentsHtml}
        </div>
      </div>

      <div style="border-top: 1px solid #e2e8f0; padding-top: 8px; margin-top: 10px;">
        <span style="font-size: 11px; color: #475569; font-weight: bold; display: block; margin-bottom: 6px;">실시간 혼잡도 제보하기</span>
        <div style="display: flex; gap: 4px;">
          <button onclick="window.reportCongestion('${festival.contentid}', '여유')" style="flex: 1; border: none; background: #e6f4ea; color: #137333; font-size: 11px; padding: 5px 0; border-radius: 4px; cursor: pointer; font-weight: bold;">여유</button>
          <button onclick="window.reportCongestion('${festival.contentid}', '보통')" style="flex: 1; border: none; background: #fef7e0; color: #b06000; font-size: 11px; padding: 5px 0; border-radius: 4px; cursor: pointer; font-weight: bold;">보통</button>
          <button onclick="window.reportCongestion('${festival.contentid}', '혼잡')" style="flex: 1; border: none; background: #fce8e6; color: #c5221f; font-size: 11px; padding: 5px 0; border-radius: 4px; cursor: pointer; font-weight: bold;">혼잡</button>
        </div>
      </div>
    </div>
  `
}

onMounted(() => {
  // 서울 중심 좌표로 지도 초기화
  map = L.map('map').setView([37.5665, 126.9780], 11)

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map)

  if (festivalData && festivalData.items) {
    // 💡 오늘 날짜를 "YYYYMMDD" 숫자 형식으로 변환 (JSON 데이터 날짜 형식과 동일하게)
    const targetDate = getEffectiveTodayNumber()

    festivalData.items.forEach((festival) => {
      const lat = parseFloat(festival.mapy)
      const lng = parseFloat(festival.mapx)

      const startDate = parseInt(festival.eventstartdate, 10)
      const endDate = parseInt(festival.eventenddate, 10)

      // 💡 오늘 날짜가 축제 기간(시작일~종료일) 안에 포함되는지 확인
      const isHappeningToday = startDate <= targetDate && endDate >= targetDate

      if (lat && lng && isHappeningToday) {
        // 가중치 연산 실행
        const { status: finalCalculatedStatus, score } = calculateCongestionFromComments(festival.communityComments)

        const marker = L.marker([lat, lng], {
          icon: createCongestionIcon(finalCalculatedStatus)
        }).addTo(map)

        marker.bindPopup(generatePopupContent(festival, finalCalculatedStatus, score))

        markersMap.set(festival.contentid, { marker, item: festival })
      }
    })
  }

  setTimeout(() => { map.invalidateSize() }, 200)
})

onUnmounted(() => {
  if (map) map.remove()
  delete window.reportCongestion
})
</script>

<style scoped>
.map-container-wrapper {
  padding: 20px;
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  margin: 20px;
}
.map-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}
.map-title {
  font-size: 18px;
  font-weight: 600;
  color: #1e293b;
  margin: 0;
}
.map-legend {
  display: flex;
  gap: 12px;
  font-size: 12px;
  font-weight: 500;
  color: #64748b;
}
.legend-item {
  display: flex;
  align-items: center;
  gap: 4px;
}
.dot {
  display: inline-block;
  width: 10px;
  height: 10px;
  border-radius: 50%;
}
.dot.green { background-color: #10b981; }
.dot.yellow { background-color: #f59e0b; }
.dot.red { background-color: #ef4444; }
.festival-map {
  width: 100%;
  height: 500px;
  border-radius: 8px;
  border: 1px solid #cbd5e1;
}
:deep(.custom-congestion-icon) {
  background: none;
  border: none;
}
</style>