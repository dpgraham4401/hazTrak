import { ProgressTracker } from 'src/components/Notifications/ProgressTracker';
import { LongRunningTask, selectAllTasks, useAppSelector } from 'src/store';

export function Notifications() {
  const tasks: LongRunningTask[] = useAppSelector(selectAllTasks);
  return (
    <>
      {tasks.map((task) => (
        <ProgressTracker task={task} key={task.taskId} />
      ))}
    </>
  );
}
