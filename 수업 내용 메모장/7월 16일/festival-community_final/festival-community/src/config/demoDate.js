// 💡 발표/시연용 날짜 설정
// 이 값을 바꾸면 지도와 게시판 전체가 그 날짜를 "오늘"로 취급합니다.
// 실제 오늘 날짜를 쓰고 싶으면 null로 바꾸세요.
export const DEMO_DATE = null

export function getEffectiveToday() {
  if (DEMO_DATE) {
    return new Date(DEMO_DATE)
  }
  return new Date()
}

// "YYYYMMDD" 숫자 형식으로 반환 (축제 JSON 데이터와 비교용)
export function getEffectiveTodayNumber() {
  const d = getEffectiveToday()
  const yyyy = d.getFullYear()
  const mm = String(d.getMonth() + 1).padStart(2, '0')
  const dd = String(d.getDate()).padStart(2, '0')
  return parseInt(`${yyyy}${mm}${dd}`, 10)
}

// 자정(하루의 끝) 기준 타임스탬프 반환 (게시글 생성시각과 비교용)
export function getEffectiveTodayEndTimestamp() {
  const d = getEffectiveToday()
  d.setHours(23, 59, 59, 999)
  return d.getTime()
}