import { http, HttpResponse } from 'msw';
import { createMockHaztrakUser } from '~/mocks/fixtures';
import {
  createMockProfileResponse,
  createMockRcrainfoProfileResponse,
} from '~/mocks/fixtures/mockUser';
import { HaztrakUser } from '~/store/authSlice/auth.slice';
import { AuthSuccessResponse } from '~/store/userSlice/user.slice';

/** mock Rest API*/
const API_BASE_URL = import.meta.env.VITE_HT_API_URL;
export const mockUserEndpoints = [
  /** GET User */
  http.get(`${API_BASE_URL}/api/auth/user/`, () => {
    return HttpResponse.json({ ...createMockHaztrakUser() }, { status: 200 });
  }),
  /** Update User */
  http.put(`${API_BASE_URL}/api/auth/user/`, (info) => {
    const user: HaztrakUser = { ...createMockHaztrakUser() };
    return HttpResponse.json({ ...user, ...info.request.body }, { status: 200 });
  }),
  /** GET Profile */
  http.get(`${API_BASE_URL}/api/profile`, () => {
    return HttpResponse.json({ ...createMockProfileResponse() }, { status: 200 });
  }),
  /** Login */
  http.post(`${API_BASE_URL}/api/user/login/`, () => {
    const body: AuthSuccessResponse = {
      access: 'mockToken',
      user: createMockHaztrakUser(),
      access_expiration: 'dateToDo',
      refresh_expiration: 'dateToDo',
      refresh: 'mockRefreshToken',
    };
    return HttpResponse.json(
      {
        ...body,
      },
      { status: 200 }
    );
  }),
  /** GET RCRAInfo profile */
  http.get(`${API_BASE_URL}/api/rcrainfo-profile/:username`, (info) => {
    const { username } = info.params;
    if (typeof username !== 'string') {
      return HttpResponse.json({}, { status: 404 });
    }
    const rcrainfoProfile = createMockRcrainfoProfileResponse({ user: username });
    return HttpResponse.json(
      {
        ...rcrainfoProfile,
      },
      { status: 200 }
    );
  }),
];
