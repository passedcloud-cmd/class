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

