// validation.js - input validation utilities
function validateTitle(title) {
  if (title == null) return '제목을 입력하세요.';
  const t = String(title).trim();
  if (t.length === 0) return '제목을 입력하세요.';
  if (t.length > 100) return '제목은 100자 이하로 입력하세요.';
  return null;
}

function validateDateTime(dateStr, timeStr) {
  if (!dateStr) return '날짜를 입력하세요.';
  // Expect date in YYYY-MM-DD and time in HH:MM (24h) or optional
  const datePattern = /^\d{4}-\d{2}-\d{2}$/;
  if (!datePattern.test(dateStr)) return '유효한 날짜 형식(YYYY-MM-DD)이 아닙니다.';
  if (timeStr) {
    const timePattern = /^\d{2}:\d{2}$/;
    if (!timePattern.test(timeStr)) return '유효한 시간 형식(HH:MM)이 아닙니다.';
    const [h, m] = timeStr.split(':').map(Number);
    if (h < 0 || h > 23 || m < 0 || m > 59) return '유효한 시간을 입력하세요.';
  }
  const date = new Date(dateStr + (timeStr ? 'T' + timeStr : ''));
  if (Number.isNaN(date.getTime())) return '유효한 날짜/시간이 아닙니다.';
  return null;
}

function validateDuration(duration) {
  if (duration == null || String(duration).trim() === '') return '소요시간을 입력하세요.';
  const n = Number(duration);
  if (!Number.isFinite(n) || n <= 0) return '소요시간은 양수 숫자여야 합니다.';
  if (!Number.isInteger(n)) return '소요시간은 정수(분)로 입력하세요.';
  return null;
}

function validateForm(fields) {
  const errors = {};
  const titleErr = validateTitle(fields.title);
  if (titleErr) errors.title = titleErr;
  const dateErr = validateDateTime(fields.date, fields.time);
  if (dateErr) errors.date = dateErr;
  if (fields.duration !== undefined) {
    const durErr = validateDuration(fields.duration);
    if (durErr) errors.duration = durErr;
  }
  return errors;
}

module.exports = {
  validateTitle,
  validateDateTime,
  validateDuration,
  validateForm,
};

// Expose for browser usage if loaded directly in a <script>
if (typeof window !== 'undefined') {
  window.__validation = {
    validateTitle,
    validateDateTime,
    validateDuration,
    validateForm,
  };
}
function validateTaskInput(rawValue) {
  // 앞뒤 공백 제거
  const value = String(rawValue ?? "").trim();

  // 빈 입력 거부
  if (value.length === 0) {
    return { valid: false, value: "", message: "빈 입력은 추가할 수 없습니다." };
  }

  // 40자 경계 판정: 40자까지 허용, 41자 이상 거부
  if (value.length > 40) {
    return { valid: false, value, message: "입력은 최대 40자까지 허용됩니다." };
  }

  return { valid: true, value };
}

if (typeof window !== "undefined") {
  window.validateTaskInput = validateTaskInput;
}

if (typeof module !== "undefined") {
  module.exports = { validateTaskInput };
}

