import '@testing-library/jest-dom';
import { QuickerSignForm } from 'src/components/Manifest/QuickerSign';
import React from 'react';
import { cleanup, renderWithProviders, screen } from 'src/test-utils';
import { createMockMTNHandler } from 'src/test-utils/fixtures';
import { afterEach, describe, expect, test } from 'vitest';

afterEach(() => {
  cleanup();
});

describe('QuickerSignForm', () => {
  test('displays the MTN to be signed', () => {
    const manifestTrackingNumbers: Array<string> = ['123456789ELC', '987654321ELC'];
    const handler = createMockMTNHandler();
    renderWithProviders(
      <QuickerSignForm mtn={manifestTrackingNumbers} mtnHandler={handler} siteType={'Generator'} />
    );
    for (const mtn of manifestTrackingNumbers) {
      expect(screen.getByText(mtn)).toBeInTheDocument();
    }
  });
  test('shows what site is signing', () => {
    const manifestTrackingNumbers: Array<string> = ['123456789ELC', '987654321ELC'];
    const handler = createMockMTNHandler();
    renderWithProviders(
      <QuickerSignForm mtn={manifestTrackingNumbers} mtnHandler={handler} siteType={'Generator'} />
    );
    expect(screen.getByText(new RegExp(`${handler.epaSiteId}`))).toBeInTheDocument();
  });
});
