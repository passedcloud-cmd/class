const {
  validateTitle,
  validateDateTime,
  validateDuration,
  validateForm,
} = require('../validation');

describe('validation', () => {
  test('validateTitle - empty', () => {
    expect(validateTitle('')).toBe('제목을 입력하세요.');
    expect(validateTitle('   ')).toBe('제목을 입력하세요.');
    expect(validateTitle(null)).toBe('제목을 입력하세요.');
  });

  test('validateTitle - length', () => {
    const long = 'a'.repeat(101);
    expect(validateTitle(long)).toBe('제목은 100자 이하로 입력하세요.');
  });

  test('validateDateTime - formats', () => {
    expect(validateDateTime('', '')).toBe('날짜를 입력하세요.');
    expect(validateDateTime('2020-13-01', '')).toMatch(/유효한 날짜/);
    expect(validateDateTime('2020-12-01', '24:00')).toMatch(/유효한 시간/);
    expect(validateDateTime('2020-12-01', '09:30')).toBeNull();
    expect(validateDateTime('2020-12-01')).toBeNull();
  });

  test('validateDuration - basic', () => {
    expect(validateDuration('')).toBe('소요시간을 입력하세요.');
    expect(validateDuration('0')).toBe('소요시간은 양수 숫자여야 합니다.');
    expect(validateDuration('-5')).toBe('소요시간은 양수 숫자여야 합니다.');
    expect(validateDuration('30.5')).toBe('소요시간은 정수(분)로 입력하세요.');
    expect(validateDuration('45')).toBeNull();
  });

  test('validateForm - aggregates', () => {
    const errs = validateForm({ title: '', date: '', time: '', duration: '' });
    expect(errs.title).toBeDefined();
    expect(errs.date).toBeDefined();
    expect(errs.duration).toBeDefined();

    const ok = validateForm({ title: 'Test', date: '2023-01-01', time: '10:00', duration: '30' });
    expect(Object.keys(ok).length).toBe(0);
  });
});
const test = require("node:test");
const assert = require("node:assert/strict");
const { validateTaskInput } = require("../validation.js");

test("공백 입력 거부", () => {
  assert.equal(validateTaskInput("   ").valid, false);
});

test("앞뒤 공백 제거", () => {
  assert.equal(validateTaskInput("  알고리즘  ").value, "알고리즘");
});

test("40자 허용", () => {
  assert.equal(validateTaskInput("가".repeat(40)).valid, true);
});

test("41자 거부", () => {
  assert.equal(validateTaskInput("가".repeat(41)).valid, false);
});

