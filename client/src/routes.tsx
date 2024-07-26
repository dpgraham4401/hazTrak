import React from 'react';
import { createBrowserRouter } from 'react-router-dom';
import { ErrorPage } from 'src/features/ErrorPage/ErrorPage';
import { Login } from 'src/features/Login';

const Dashboard = React.lazy(() => import('src/features/Dashboard'));
const Profile = React.lazy(() => import('src/features/Profile'));
const SiteList = React.lazy(() => import('src/features/SiteList'));
const SiteDetails = React.lazy(() => import('src/features/SiteDetails'));
const Help = React.lazy(() => import('src/features/About'));

export const router = createBrowserRouter([
  {
    path: '/',
    lazy: () => import('./components/Layout'),
    children: [
      {
        path: '',
        element: <Dashboard />,
      },
      {
        path: '/profile',
        element: <Profile />,
      },
      {
        path: '/site',
        children: [
          {
            path: '',
            element: <SiteList />,
          },
          {
            path: ':siteId',
            element: <SiteDetails />,
          },
          {
            path: ':siteId/manifest',
            children: [
              {
                path: '',
                lazy: () => import('./features/ManifestList'),
              },
              {
                path: 'new',
                lazy: () => import('./features/NewManifest'),
              },
              {
                path: ':mtn/:action',
                lazy: () => import('./features/ManifestDetails'),
              },
            ],
          },
        ],
      },
      {
        path: '/manifest',
        children: [
          {
            path: '',
            lazy: () => import('./features/ManifestList'),
          },
          {
            path: 'new',
            lazy: () => import('./features/NewManifest'),
          },
          {
            path: ':mtn/:action',
            lazy: () => import('./features/ManifestDetails'),
          },
        ],
      },
      {
        path: '/about',
        element: <Help />,
      },
    ],
  },
  {
    path: '/login',
    element: <Login />,
  },
  {
    path: '/register',
    lazy: () => import('./features/RegisterHero'),
  },
  {
    path: '*',
    element: <ErrorPage code={404} />,
  },
]);
