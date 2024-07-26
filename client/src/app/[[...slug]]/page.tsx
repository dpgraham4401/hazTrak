import '../../App.scss';
import { ClientOnly } from 'src/app/[[...slug]]/client';

export function generateStaticParams() {
  return [{ slug: [''] }];
}

export default function Page() {
  return <ClientOnly />;
}
