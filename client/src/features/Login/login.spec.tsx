import '@testing-library/jest-dom';
import React from 'react';
import { Login } from 'src/features/Login';
import { renderWithProviders, screen } from 'src/test-utils';
import { describe, expect, test } from 'vitest';

describe('Login component', () => {
  test('renders', () => {
    renderWithProviders(<Login />, {});
    expect(screen.getByRole('button', { name: 'Login' })).toBeInTheDocument();
    expect(screen.getByLabelText('Username')).toBeInTheDocument();
    expect(screen.getByLabelText('Password')).toBeInTheDocument();
  });
});
